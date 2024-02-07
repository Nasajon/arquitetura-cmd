import datetime
import logging
import uuid

from abc import ABC, abstractmethod
from suporte_console.db_adapter2 import DBAdapter2
from typing import Any, Callable, Dict, List, Tuple

from suporte_console.diagnostico_conjuntos.registros import REGISTROS_DICT_REVERSE


class PatchParticipantesCompartilhados(ABC):
    """
    Superclasse para resolver um problema de quando um participante
    está indevidamente compartilhado por mais de um conjunto.

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
        1. Selecionar os dados indevidamente compartilhados
        2. Para cada dado:
        2.1. Descobrir o conjunto com maior uso do participante (contando títulos e docfis relacionados)
        2.2. Guardar num buffer os conjuntos associados
        2.3. Apagar as associações com os conjuntos (com exceção do conjunto com maior uso)
        2.4. Replicar o participante para cada um dos outros conjuntos
        2.5. Associar cada cópia com o respectivo conjunto
        2.6. Copiar endereços, contatos e telefones, para cada cópia do participante
        """

        # Getting logger
        logger = logging.getLogger('diagnostico_conjuntos')

        # Recuperando os dados compartilhados
        logger.info(
            'Recuperando a lista de registros compartilhados com mais de um conjunto.')
        compartilhados = self.list_dados_compartilhados(registro_tipo)

        if len(compartilhados) <= 0:
            logger.info(
                'Não foram encontrados resgitros compartilhados com mais de um conjunto.')
            return

        # Recuperando lista de IDs a ignorar
        dados_ignorar = self.list_dados_ignorar(registro_tipo)

        # Iterando os dados compartilhados
        for dado in compartilhados:
            id = dado['id']

            if id in (dados_ignorar):
                logger.info(
                    f"Pulando o dado {id}, por estar na lista de dados a ignorar")
                continue

            # Descobrindo o conjunto com maior uso
            logger.info(
                'Identificando o estabelecimento com maior uso do registro (para deixar o registro original no conjunto associado).')
            maior_uso = self.get_estabelecimento_maior_uso(registro_tipo, id)

            if maior_uso is not None:
                conjunto_maior_uso = self.get_conjunto(
                    registro_tipo, maior_uso['estabelecimento'])
            else:
                conjunto_maior_uso = None

            # Recuperando os conjuntos associados
            logger.info(
                'Recuperando todos os conjuntos associados com o registro.')
            conjuntos_associados = self.get_conjuntos_associados(
                registro_tipo, id)

            if conjunto_maior_uso is None and len(conjuntos_associados) > 0:
                # Se não há um conjunto de maior uso, seleciona um aleatório
                conjunto_maior_uso = {
                    'conjunto': conjuntos_associados[0]['conjunto']}

            # Apagando as associações com os conjuntos
            logger.info(
                'Apagando as associações indevidas do dado com os conjuntos (mantendo apenas a associação com o conjunto de maior uso).')
            self.apaga_associacoes_conjuntos(
                registro_tipo, id, conjunto_maior_uso['conjunto'])

            # Recuperando o conjunto de fichas de maior uso
            logger.info(
                'Recuperando o conjunto de fichas, associado ao estabelecimento de maior uso do dado.')
            conjunto_ficha_maior_uso = self.get_conjunto_ficha(
                conjunto_maior_uso['conjunto'])

            # Apagando as associações com os conjuntos de fichas
            logger.info(
                'Apagando as associações com os conjuntos de fichas (com exceção do conjutno do estabelecimento que mais usa o dado).')
            self.apaga_associacoes_conjuntos(
                'fichas', id, conjunto_ficha_maior_uso['conjunto'])

            # Iterando as antigas associações
            logger.info(
                'Copiando o dado para cada um dos conjuntos antes associados')
            for conj_assoc in conjuntos_associados:
                if conj_assoc['conjunto'] == conjunto_maior_uso['conjunto']:
                    continue

                # Criando uma cópia do participante para o conjunto
                logger.info('Inserindo uma cópia do dado')
                dado = self.copiar_dado('ns', 'pessoas', 'id', id,
                                        self.ajusta_pessoa_para_novo_registro, {})

                # Associando o novo participante ao conjunto
                logger.info('Associando a cópia a um dos conjuntos')
                self.associa_dado_conjunto(
                    registro_tipo, dado['id'], conj_assoc['conjunto'])

                # Recuperando o conjunto de fichas
                conjunto_ficha = self.get_conjunto_ficha(
                    conj_assoc['conjunto'])

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

    def list_dados_compartilhados(self, registro: str):
        """
        Retorna uma lista de registros associados a mais de um conjunto.
        """

        sql = f"""
        select
            assoc.registro as id
        from ns.conjuntos{registro} as assoc
        group by assoc.registro
        having count(*) > 1
        """

        return self.db_adapter.execute_query(sql)

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

    def get_conjunto(self, registro: str, estabelecimento: uuid.UUID):
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

        cadastro = REGISTROS_DICT_REVERSE[registro]

        result = self.db_adapter.execute_query(
            sql, estabelecimento=estabelecimento, cadastro=cadastro)

        if len(result) > 1:
            raise Exception(
                f"Mais de um conjunto do registro {registro}, encontrado para o estabelecimento: {estabelecimento}")

        if len(result) <= 0:
            raise Exception(
                f"Não foi encontrado um conjunto do registro {registro}, para o estabelecimento: {estabelecimento}")

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

    def get_conjuntos_associados(self, registro: str, id: uuid.UUID):
        """
        Recuperando todos os IDs dos conjuntos associados ao dado com ID "id",
        e considerando o tipo de "registro".
        """

        sql = f"""
        select
            assoc.conjunto
        from
            ns.conjuntos{registro} as assoc
        where
            assoc.registro = :id
        """

        return self.db_adapter.execute_query(sql, id=id)

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

    # def list_column_from_table(self, schema: str, table: str) -> List[Dict[str, Any]]:
    #     sql = """
    #         select
    #             column_name, data_type
    #         from
    #             INFORMATION_SCHEMA.COLUMNS
    #         where
    #             table_schema = :schema
    #             and table_name = :table
    #     """

    #     return self.db_adapter.execute_query(sql, schema=schema, table=table)

    def associa_dado_conjunto(self, registro: str, id: uuid.UUID, conjunto: uuid.UUID):
        """
        Associa do dado representado pelo "id", ao conjunto "conjunto" (considerando
        o tipo de "registro" passado).
        """

        sql = f"""
        insert into ns.conjuntos{registro} (registro, conjunto)
        values (:id, :conjunto)
        """
        self.db_adapter.execute(sql, id=id, conjunto=conjunto)

    def apaga_associacoes_conjuntos(self, registro: str, id: uuid.UUID, conjunto_excecao: uuid.UUID):
        """
        Exclui as associações do dado representado pelo "id", com qualquer conjunto do tipo
        "registro", com exceção do conjunto com id "conjunto_excecao".
        """

        sql = f"""
        delete from ns.conjuntos{registro} where registro = :id and conjunto <> :conjunto
        """
        self.db_adapter.execute(sql, id=id, conjunto=conjunto_excecao)
