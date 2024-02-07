import datetime
import logging
import uuid

from abc import ABC, abstractmethod
from suporte_console.db_adapter2 import DBAdapter2
from typing import Any, Callable, Dict, List, Tuple

from suporte_console.diagnostico_conjuntos.registros import REGISTROS_DICT_REVERSE


class PatchConjuntosParticipantesCompartilhados(ABC):
    """
    Superclasse para resolver um problema de quando um conjunto de participantes
    está indevidamente compartilhado por mais de uma empresa, ou grupo empresarial.

    As sub-classes é que tratarão de cada tipo de participante
    """

    def __init__(self, db_adapter: DBAdapter2) -> None:
        self.db_adapter = db_adapter

    @abstractmethod
    def can_execute(self, registro_tipo: str) -> bool:
        pass

    def execute(self, registro_tipo: str):
        """
        A estratégia aqui é:
        1. Selecionar os conjuntos indevidamente compartilhados
        2. Selecionar os dados indevidamente compartilhados
        3. Para cada dado:
        3.1. Descobrir o conjunto com maior uso do participante (contando títulos e docfis relacionados)
        3.2. Guardar num buffer os conjuntos associados
        3.3. Apagar as associações com os conjuntos (com exceção do conjunto com maior uso)
        3.4. Replicar o participante para cada um dos outros conjuntos
        3.5. Associar cada cópia com o respectivo conjunto
        3.6. Copiar endereços, contatos e telefones, para cada cópia do participante
        """

        # Getting logger
        logger = logging.getLogger('diagnostico_conjuntos')

        # Recuperando os conjuntos indevidamente compartilhados
        logger.info(
            'Recuperando os conjuntos indevidamente compartilhados')
        conjuntos_compartilhados = self.list_conjuntos_compartilhados(
            registro_tipo)

        # Iterando os conjuntos compartilhados
        for conjunto_compartilhado in conjuntos_compartilhados:

            # Recuperando a lista de estabelecimentos associados ao conjunto
            logger.info(
                'Recuperando a lista de estabelecimentos associados ao conjunto.')
            estabelecimentos_associados = self.list_estabelecimentos_associados(
                conjunto_compartilhado['conjunto'])

            # Verificando se cada estabelecimento tem seu próprio conjunto para o tipo de registro
            logger.info(
                'Verificando se cada estabelecimento tem seu próprio conjunto para o tipo de registro')
            self.verifica_existencia_conjuntos(
                registro_tipo, conjunto_compartilhado, estabelecimentos_associados)

            # Recuperando os dados do conjunto compartilhado
            logger.info(
                'Recuperando a lista dos registros do conjunto compartilhado.')
            dados = self.list_dados_conjunto(
                registro_tipo, conjunto_compartilhado['conjunto'])

            if len(dados) <= 0:
                logger.info(
                    'Não foram encontrados registros no conjunto compartilhado.')

            # Recuperando lista de IDs a ignorar
            dados_ignorar = self.list_dados_ignorar(registro_tipo)

            # Iterando os dados a copiar
            for dado in dados:
                id = dado['id']

                if id in (dados_ignorar):
                    logger.info(
                        f"Pulando o dado {id}, por estar na lista de dados a ignorar")
                    continue

                # Descobrindo o estabelecimento com maior uso
                logger.info(
                    'Identificando o estabelecimento com maior uso do registro (para deixar o registro original no conjunto associado).')
                maior_uso = self.get_estabelecimento_maior_uso(
                    registro_tipo, id)

                # Se não foi identificado um estabelecimento com maior uso,
                # seleciona um aleatório (dentre os associados)
                if maior_uso is None and len(estabelecimentos_associados) > 0:
                    maior_uso = estabelecimentos_associados[0]

                # Copiando o registro para cada um dos estabelecimentos (que não o de maior uso)
                for estab in estabelecimentos_associados:
                    logger.info(
                        f"Copiando o dado para o estabelecimento {estab['estabelecimento']}")

                    # Recuperando o conjunto do estabelecimento de destino
                    conjunto_destino = self.get_conjunto(
                        registro_tipo, estab['estabelecimento'], conjunto_compartilhado['conjunto'])

                    # Verificando se é o estabelecimento de maior uso
                    if estab['estabelecimento'] == maior_uso['estabelecimento']:
                        # Se for o caso, apenas faz a associação, sem copiar o registro
                        self.associa_dado_conjunto(
                            registro_tipo, id, conjunto_destino['conjunto'])
                        continue

                    # Criando uma cópia do participante para o conjunto
                    logger.info('Inserindo uma cópia do dado')
                    dado = self.copiar_dado('ns', 'pessoas', 'id', id,
                                            self.ajusta_pessoa_para_novo_registro, {})

                    # Associando o novo participante ao conjunto
                    logger.info('Associando a cópia a um dos conjuntos')
                    self.associa_dado_conjunto(
                        registro_tipo, dado['id'], conjunto_destino['conjunto'])

                    # Recuperando o conjunto de fichas
                    conjunto_ficha = self.get_conjunto_ficha(
                        conjunto_destino['conjunto'])

                    # Associando o novo participante ao conjunto de fichas
                    self.associa_dado_conjunto(
                        'fichas', dado['id'], conjunto_ficha['conjunto'])

                    # Copiando os endereços do participante
                    logger.info('Copiando os endereços do participante')
                    enderecos = self.list_enderecos(id)
                    for endereco in enderecos:
                        self.copiar_dado('ns', 'enderecos', 'endereco', endereco['endereco'],
                                         self.ajusta_endereco_para_novo_registro, {'id_pessoa': dado['id']})

                    # Copiando os contatos do participante
                    logger.info('Copiando os contatos do participante')
                    contatos = self.list_contatos(id)
                    for contato in contatos:
                        id_contato_old = contato['id']
                        self.copiar_dado('ns', 'contatos', 'id', contato['id'],
                                         self.ajusta_contato_para_novo_registro, {'id_pessoa': dado['id']})

                        # Copiando os telefones do contato
                        logger.info(
                            'Copiando os telefones de um dos contatos do participante')
                        telefones = self.list_telefones(id_contato_old)
                        for telefone in telefones:
                            self.copiar_dado('ns', 'telefones', 'id', telefone['id'],
                                             self.ajusta_telefone_para_novo_registro, {'id_pessoa': dado['id'], 'id_contato': contato['id']})

                    # Copiando os telefones sem contato
                    logger.info(
                        'Copiando os telefones do participante (sem contato associado).')
                    telefones = self.list_telefones_sem_contato(id)
                    for telefone in telefones:
                        self.copiar_dado('ns', 'telefones', 'id', telefone['id'],
                                         self.ajusta_telefone_para_novo_registro, {'id_pessoa': dado['id'], 'id_contato': None})

            ################
            # Apagando o conjunto compartilhado (após resolvidos os dados do mesmo)
            ################

            # Apagando as associações do conjunto com os dados
            logger.info(
                'Apagando as associações do conjunto compartilhado, já resolvido, com os dados.')
            self.apaga_associacoes_conjunto(
                registro_tipo, conjunto_compartilhado['conjunto'])

            # Apagando as associações do conjunto com os estabelecimentos
            logger.info(
                'Apagando as associações do conjunto compartilhado com estabelecimentos.')
            self.apaga_associacoes_estabelecimentos_conjunto(
                registro_tipo, conjunto_compartilhado['conjunto'])

            # Apagando o conjunto em si
            logger.info(
                'Apagando as associações do conjunto compartilhado, já resolvido.')
            self.apaga_conjunto(
                registro_tipo, conjunto_compartilhado['conjunto'])

    def verifica_existencia_conjuntos(self, registro_tipo, conjunto_compartilhado, estabelecimentos_associados):
        for est_assoc in estabelecimentos_associados:
            # Procurando o conjunto associado ao estabelecimento
            conj_assoc = self.get_conjunto(
                registro_tipo,
                est_assoc['estabelecimento'],
                conjunto_compartilhado['conjunto'],
                True
            )

            if conj_assoc is None:
                # Procurando o conjunto associado ao qualquer estabelecimento
                # da mesma empresa ou grupo (de acordo com o modo da instalação)
                conj_assoc = self.get_conjunto_empresa_ou_grupo(
                    registro_tipo,
                    est_assoc['estabelecimento'],
                    conjunto_compartilhado['conjunto']
                )

                if conj_assoc is not None:
                    # Se achou, é porque faltava estar associado com o estabelecimento,
                    # então só associa
                    self.associa_conjunto_estabelecimento(
                        registro_tipo, est_assoc['estabelecimento'], conj_assoc['conjunto'])

            if conj_assoc is None:
                # Se ainda não achou, então cria um novo conjunto, e o associa a todos
                # os estabelecimentos do mesmo grupo ou empresa (de acordo com o modo de instalação)
                conj_assoc = self.cria_conjunto_estabelecimento(
                    registro_tipo, est_assoc['estabelecimento'])

    def ajusta_contato_para_novo_registro(self, dado: Dict[str, Any], aux_data: Dict[str, Any]):
        """
        Prepara um dict, representando um contato, para ser novamente inserido no BD,
        porém como uma cópia do contato do participante sendo copiado.
        """

        dado['id'] = str(uuid.uuid4())
        dado['id_pessoa'] = aux_data['id_pessoa']

    def ajusta_telefone_para_novo_registro(self, dado: Dict[str, Any], aux_data: Dict[str, Any]):
        """
        Prepara um dict, representando um telefone, para ser novamente inserido no BD,
        porém como uma cópia do telefone do participante sendo copiado, ou cópia do telefone do
        contato sendo copiado.
        """

        dado['id'] = str(uuid.uuid4())
        dado['contato'] = aux_data['id_contato']
        dado['id_pessoa'] = aux_data['id_pessoa']

    def ajusta_endereco_para_novo_registro(self, dado: Dict[str, Any], aux_data: Dict[str, Any]):
        """
        Prepara um dict, representando um endereço, para ser novamente inserido no BD,
        porém como uma cópia do endereço do participante sendo copiado.
        """

        dado['endereco'] = str(uuid.uuid4())
        dado['id_pessoa'] = aux_data['id_pessoa']

    def ajusta_pessoa_para_novo_registro(self, dado: Dict[str, Any], aux_data: Dict[str, Any]):
        """
        Prepara um dict, representando um participante, para ser novamente inserido no BD,
        porém como uma cópia do participante representado.
        """

        dado['id'] = str(uuid.uuid4())
        dado['datacadastro'] = datetime.date.today()
        dado['datacriacao'] = datetime.date.today()
        # TODO Tratar do código do participante?

    def list_telefones_sem_contato(self, id_pessoa: uuid.UUID) -> List[Dict[str, Any]]:
        """
        Retornando a lista de IDs dos telefones relacionados a um participante (sem contato associado).
        """

        sql = """
        select id from ns.telefones where contato is null and id_pessoa=:id_pessoa
        """
        return self.db_adapter.execute_query(sql, id_pessoa=id_pessoa)

    def list_telefones(self, id_contato: uuid.UUID) -> List[Dict[str, Any]]:
        """
        Retornando a lista de IDs dos telefones relacionados a um contato de um participante
        """

        sql = """
        select id from ns.telefones where contato=:id_contato
        """
        return self.db_adapter.execute_query(sql, id_contato=id_contato)

    def list_contatos(self, id_pessoa: uuid.UUID) -> List[Dict[str, Any]]:
        """
        Retornando a lista de IDs dos contatos relacionados a um participante
        """

        sql = """
        select id from ns.contatos where id_pessoa=:id_pessoa
        """
        return self.db_adapter.execute_query(sql, id_pessoa=id_pessoa)

    def list_enderecos(self, id_pessoa: uuid.UUID) -> List[Dict[str, Any]]:
        """
        Retornando a lista de IDs dos endereços relacionados a um participante
        """

        sql = """
        select endereco from ns.enderecos where id_pessoa=:id_pessoa
        """
        return self.db_adapter.execute_query(sql, id_pessoa=id_pessoa)

    @abstractmethod
    def list_dados_ignorar(self, registro: str):
        """
        Retorna uma lista de uuids, com os dados que não precisam
        ser tratados com relação ao compartilhamento entre conjuntos.
        """
        pass

    def list_dados_conjunto(self, registro: str, conjunto: uuid.UUID):
        """
        Retorna a lista de registros associados ao conjunto recebido (do tipo "registro")
        """

        sql = f"""
        select
            assoc.registro as id
        from
            ns.conjuntos{registro} as assoc
        where
            assoc.conjunto = :conjunto
        """

        return self.db_adapter.execute_query(sql, conjunto=conjunto)

    @abstractmethod
    def get_estabelecimento_maior_uso(self, registro: str, id: uuid.UUID):
        """
        Método que deve ser extendido para retornar um dict contendo a propriedade
        "estabelecimento", a qual denote o estabelecimento com maior uso do dado
        com "id" recebido (cujo tipo de registro é recebido no argumento "registro").

        Pode-se imaginar uma implementação desse método, contando títulos e notas fiscais
        associadas ao dado.
        """
        pass

    def get_conjunto(self, registro: str, estabelecimento: uuid.UUID, conjunto_indesejado: uuid.UUID = None, retornar_none: bool = False):
        """
        Recupera o conjunto associado ao "estabelecimento" e "registro" passado,
        retornando o ID do conjunto (num dict com a propriedade "conjunto").
        """

        sql = f"""
        select
            conjunto
        from
            ns.estabelecimentosconjuntos as ec
        where
            ec.estabelecimento = :estabelecimento
            and ec.cadastro = :cadastro
        """

        if conjunto_indesejado is not None:
            sql += " and ec.conjunto <> :conjunto_indesejado "

        cadastro = REGISTROS_DICT_REVERSE[registro]

        result = self.db_adapter.execute_query(
            sql, estabelecimento=estabelecimento, cadastro=cadastro, conjunto_indesejado=conjunto_indesejado)

        if len(result) > 1:
            raise Exception(
                f"Mais de um conjunto do registro {registro}, encontrado para o estabelecimento: {estabelecimento}")

        if len(result) <= 0:
            if retornar_none:
                return None
            else:
                raise Exception(
                    f"Não foi encontrado um conjunto do registro {registro}, para o estabelecimento: {estabelecimento}")

        return result[0]

    def get_conjunto_empresa_ou_grupo(self, registro: str, estabelecimento: uuid.UUID, conjunto_indesejado: uuid.UUID):
        """
        Recupera o conjunto associado a empresa ou grupo empresarial (de acordo com o modo de instalação),
        do "estabelecimento" e "registro" passado, retornando o ID do conjunto (num dict com a propriedade "conjunto").
        """

        if not self.is_modo_empresa():
            sql = f"""
            with estabelecimentos_associados as (
                select
                    est2.estabelecimento
                from
                    ns.estabelecimentos as est
                    join ns.estabelecimentos as est2 on (est2.empresa = est.empresa and est2.estabelecimento <> est.estabelecimento)
                where
                    est.estabelecimento = :estabelecimento
            )
            select
                ec.conjunto
            from
                ns.estabelecimentosconjuntos as ec
                join estabelecimentos_associados as est on (est.estabelecimento = ec.estabelecimento)
            where
                ec.cadastro = :cadastro
                and ec.conjunto <> :conjunto_indesejado
            """
        else:
            sql = f"""
            with estabelecimentos_associados as (
                select
                    est2.estabelecimento
                from
                    ns.estabelecimentos as est
                    join ns.empresas as emp on (emp.empresa = est.empresa)
                    join ns.empresas as emp2 on (emp2.grupoempresarial = emp.grupoempresarial)
                    join ns.estabelecimentos as est2 on (est2.empresa = emp2.empresa and est2.estabelecimento <> est.estabelecimento)
                where
                    est.estabelecimento = :estabelecimento
            )
            select
                ec.conjunto
            from
                ns.estabelecimentosconjuntos as ec
                join estabelecimentos_associados as est on (est.estabelecimento = ec.estabelecimento)
            where
                ec.cadastro = :cadastro
                and ec.conjunto <> :conjunto_indesejado
            """

        cadastro = REGISTROS_DICT_REVERSE[registro]

        result = self.db_adapter.execute_query(
            sql, estabelecimento=estabelecimento, cadastro=cadastro, conjunto_indesejado=conjunto_indesejado)

        if len(result) > 1:
            raise Exception(
                f"Mais de um conjunto do registro {registro}, encontrado para o estabelecimento: {estabelecimento}")

        if len(result) <= 0:
            return None

        return result[0]

    def get_conjunto_ficha(self, conjunto: uuid.UUID):
        """
        Recupera o conjunto ficha equivalente ao conjunto recebido.
        """

        sql = f"""
        with estabelecimentos_associados as (
            select
                distinct estabelecimento
            from
                ns.estabelecimentosconjuntos
            where
                conjunto = :conjunto
        )
        select
            distinct conjunto
        from
            ns.estabelecimentosconjuntos as ec
            join estabelecimentos_associados as ea
                on (ea.estabelecimento = ec.estabelecimento)
        where
            ec.cadastro = :cadastro
        """

        cadastro = REGISTROS_DICT_REVERSE['fichas']

        result = self.db_adapter.execute_query(
            sql, conjunto=conjunto, cadastro=cadastro)

        if len(result) > 1:
            raise Exception(
                f"Mais de um conjunto ficha equivalente ao conjunto: {conjunto}")

        if len(result) <= 0:
            raise Exception(
                f"Não foi encontrado um conjunto ficha equivalente ao conjunto: {conjunto}")

        return result[0]

    def copiar_dado(self, schema: str, tabela: str, pk_column: str, id: uuid.UUID, ajusta_dados_para_novo_registro: Callable, aux_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Copiando o dado com ID "id", na tabela "schema"."tabela", cuja coluna chave primária seja a "pk_column".

        Para esse processo, o método passado no parâmetro "ajusta_dados_para_novo_registro" é chamado para
        ajustar os dados (dict) da cópia a ser inserida no BD, e o dict "aux_data" é passado para
        esse mesmo método, de mdo que dados de relacionamento possam ser cosiderados no ajuste dos dados a copiar.
        """

        # Getting logger
        logger = logging.getLogger('diagnostico_conjuntos')

        # Recuperando o dado
        logger.info(f"Recuperando o dado a copiar. Tabela: {schema}.{tabela}")
        dado = self.get_dado(id, schema, tabela, pk_column)

        # Criando uma lista das colunas da tabela
        colunas = [k for k in dado]

        # Montando o sql para insert
        logger.info('Preparando insert de duplicação do dado')
        buffer_columns, buffer_values = self.build_columns_values_for_insert(
            colunas)
        sql = f"""
        insert into {schema}.{tabela} ({buffer_columns})
        values ({buffer_values})
        """

        # Ajustando os dados para o novo registro
        logger.info('Ajustando os dados para o novo registro')
        ajusta_dados_para_novo_registro(dado, aux_data)

        # Processando o insert
        logger.info('Inserindo a cópia do dado.')
        self.db_adapter.execute(sql, **dado)

        # Retornando o dado inserido
        return dado

    def get_dado(self, id: uuid.UUID, schema: str, tabela: str, pk_column: str) -> Dict[str, Any]:
        """
        Recupera, num dict, o registro completo da tabela "schema"."tabela", onde
        a chave primária seja a coluna "pk_column", e tenha o valor "id".
        """

        sql = f"""
        select * from {schema}.{tabela} where {pk_column}=:id
        """
        return self.db_adapter.execute_query_first_result(sql, id=id)

    def build_columns_values_for_insert(self, columns: List[str]) -> Tuple[str, str]:
        """
        Monta a parte de colunas e valores de um insert, retornando
        essas partes numa tupla: Tuple[str, str] -> (colunas, valores)

        Obs.: A parte de valores é quase igual a de colunas, sendo que adicionando
        um caracter ":" no início de cada nome de coluna, para permitir o binding
        dos dados na execução da query.
        """

        buffer_columns = ''
        buffer_values = ''

        for column in columns:
            if len(buffer_columns) > 0:
                buffer_columns += ','
                buffer_values += ','

            buffer_columns += column
            buffer_values += f":{column}"

        return (buffer_columns, buffer_values)

    def associa_dado_conjunto(self, registro: str, id: uuid.UUID, conjunto: uuid.UUID):
        """
        Associa do dado representado pelo "id", ao conjunto "conjunto" (considerando
        o tipo de "registro" passado).
        """

        sql = f"""
        insert into ns.conjuntos{registro} (registro, conjunto)
        select :id, :conjunto where not exists
        (select 1 from ns.conjuntos{registro} where registro=:id and conjunto=:conjunto)
        """
        self.db_adapter.execute(sql, id=id, conjunto=conjunto)

    def apaga_associacoes_conjunto(self, registro: str, conjunto: uuid.UUID):
        """
        Exclui todas as associações de dados com o "conjunto" do tipo "registro".
        """

        sql = f"""
        delete from ns.conjuntos{registro} where conjunto = :conjunto
        """
        self.db_adapter.execute(sql, id=id, conjunto=conjunto)

    def apaga_associacoes_estabelecimentos_conjunto(self, registro: str, conjunto: uuid.UUID):
        """
        Exclui todas as associações dos estabelecimentos com o "conjunto" do tipo "registro".
        """

        sql = f"""
        delete from ns.estabelecimentosconjuntos where conjunto = :conjunto and cadastro = :cadastro
        """

        cadastro = REGISTROS_DICT_REVERSE[registro]
        self.db_adapter.execute(sql, conjunto=conjunto, cadastro=cadastro)

    def apaga_conjunto(self, registro: str, conjunto: uuid.UUID):
        """
        Exclui o "conjunto" do tipo "registro".
        """

        sql = f"""
        delete from ns.conjuntos where conjunto = :conjunto and cadastro = :cadastro
        """

        cadastro = REGISTROS_DICT_REVERSE[registro]
        self.db_adapter.execute(sql, conjunto=conjunto, cadastro=cadastro)

    def is_modo_empresa(self):
        """
        Retorna true se o BD estiver em modo empresa, e false, caso contrário.
        """

        sql = """
        SELECT VALOR as modo FROM NS.CONFIGURACOES WHERE CAMPO = 1 AND APLICACAO = 0
        """

        modo = self.db_adapter.execute_query_first_result(sql)

        if str(modo['modo']) == '0':
            return True
        else:
            return False

    def list_conjuntos_compartilhados(self, registro: str) -> List[Dict[str, Any]]:
        """
        Retorna a lista de conjuntos, do tipo de "registro", que estejam indevidamente compartilhados
        entre grupo empresariais, ou empresas (de acordo com o modo de instalação).
        """

        if self.is_modo_empresa():
            sql = """
            with conjuntos_grupos_empresariais as (
                select
                    distinct emp.grupoempresarial, ec.conjunto
                from
                    ns.estabelecimentosconjuntos as ec
                    join ns.estabelecimentos as est on (est.estabelecimento = ec.estabelecimento)
                    join ns.empresas as emp on (emp.empresa = est.empresa)
                where
                    ec.cadastro = :cadastro
            )
            select ce.conjunto from conjuntos_grupos_empresariais as ce group by ce.conjunto having count(*) > 1
            """
        else:
            sql = """
            with conjuntos_empresas as (
                select
                    distinct est.empresa, ec.conjunto
                from
                    ns.estabelecimentosconjuntos as ec
                    join ns.estabelecimentos as est on (est.estabelecimento = ec.estabelecimento)
                where
                    ec.cadastro = :cadastro
            )
            select ce.conjunto from conjuntos_empresas as ce group by ce.conjunto having count(*) > 1
            """

        cadastro = REGISTROS_DICT_REVERSE[registro]

        return self.db_adapter.execute_query(sql, cadastro=cadastro)

    def list_estabelecimentos_associados(self, conjunto: uuid.UUID) -> List[Dict[str, Any]]:
        """
        Retorna a lista de estabelecimentos associados ao conjunto.
        """

        sql = """
        select
            distinct estabelecimento
        from
            ns.estabelecimentosconjuntos
        where
            conjunto = :conjunto
        """

        return self.db_adapter.execute_query(sql, conjunto=conjunto)

    def cria_conjunto_estabelecimento(self, registro: str, estabelecimento: uuid.UUID):
        """
        Cria um novo conjunto associado ao estabelecimento passado, de acordo com o modo de instalação.
        """

        cadastro = REGISTROS_DICT_REVERSE[registro]

        # Recupera os dados do grupo ou empresa
        if not self.is_modo_empresa():
            sql = """
            select
                emp.codigo
            from
                ns.estabelecimentos as est
                join ns.empresas as emp on (emp.empresa = est.empresa)
            where
                est.estabelecimento = :estabelecimento
            """
        else:
            sql = """
            select
                ge.codigo
            from
                ns.estabelecimentos as est
                join ns.empresas as emp on (emp.empresa = est.empresa)
                join ns.gruposempresariais as ge on (ge.grupoempresarial = emp.grupoempresarial)
            where
                est.estabelecimento = :estabelecimento
            """

        dados_conjunto = self.db_adapter.execute_query_first_result(
            sql, estabelecimento=estabelecimento)

        # Inserindo o novo conjunto em si
        sql = """
        insert into ns.conjuntos (conjunto, descricao, cadastro, codigo) values (:conjunto, :descricao, :cadastro, :codigo)
        """

        codigo = f"{dados_conjunto['codigo']}{dados_conjunto['codigo']}"
        conjunto = uuid.uuid4()

        self.db_adapter.execute(sql, conjunto=conjunto, descricao=codigo,
                                cadastro=cadastro, codigo=codigo)

        # Listando os estabelecimentos a associar
        if not self.is_modo_empresa():
            sql = """
            select
                est2.estabelecimento
            from
                ns.estabelecimentos as est
                join ns.estabelecimentos as est2 on (est.empresa = est2.empresa)
            where
                est.estabelecimento = :estabelecimento
            """
        else:
            sql = """
            select
                est2.estabelecimento
            from
                ns.estabelecimentos as est
                join ns.empresas as emp on (emp.empresa = est.empresa)
                join ns.empresas as emp2 on (emp2.grupoempresarial = emp.grupoempresarial)
                join ns.estabelecimentos as est2 on (est2.empresa = emp2.empresa)
            where
                est.estabelecimento = :estabelecimento
            """

        estabs = self.db_adapter.execute_query(
            sql, estabelecimento=estabelecimento)

        # Associando o novo conjunto a cada estabelecimento
        for est in estabs:
            self.associa_conjunto_estabelecimento(
                registro, est['estabelecimento'], conjunto)

        # Retornando o conjunto criado
        return {'conjunto': conjunto}

    def associa_conjunto_estabelecimento(self, registro: str, estabelecimento: uuid.UUID, conjunto: uuid.UUID):
        """
        Insere uma associação entre um conjunto e um estabelecimento, na tabela ns.estabelecimentosconjuntos
        """

        cadastro = REGISTROS_DICT_REVERSE[registro]

        sql = """
        insert into ns.estabelecimentosconjuntos (estabelecimento, conjunto, cadastro, permissao)
        values (:estabelecimento, :conjunto, :cadastro, true)
        """

        self.db_adapter.execute(
            sql, estabelecimento=estabelecimento, conjunto=conjunto, cadastro=cadastro)
