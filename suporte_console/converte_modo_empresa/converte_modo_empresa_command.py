import time
import uuid

from typing import Any, Dict, List

from suporte_console.command import Command


class ConverteModoEmpresaCommand(Command):

    # Dicionário entre a numeração dos cadastros, e suas respectivas tabelas de associação com os dados:
    CADASTROS = {
        0: 'conjuntosprodutos',
        1: 'conjuntosunidades',
        2: 'conjuntoscombustiveis',
        3: 'conjuntosservicos',
        4: 'conjuntosclassificacoesparticipantes',
        5: 'conjuntosfichas',
        6: 'conjuntosclientes',
        7: 'conjuntosfornecedores',
        8: 'conjuntostransportadoras',
        9: 'conjuntosvendedores',
        10: 'conjuntosservicosdecatalogos',
        11: 'conjuntosmodeloscontratos',
        12: 'conjuntostecnicos',
        13: 'conjuntosrubricas',
        14: 'conjuntosrepresentantescomerciais',
        15: 'conjuntosrepresentantestecnicos',
        16: 'conjuntosprospects'
    }

    def ajusta_persmissoes_group_nasajon(self):
        """
        Roda a função ns.permissoes, para ajustar as permissões do BD.
        """

        try:
            sql = f"select * from ns.permissoes()"
            self.db_adapter.execute(sql)
        except Exception as e:
            self.log_warning(
                f"Erro manipulando permissões do BD clonado: {e}")

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

    def set_modo_empresa(self):
        """
        Atualiza a flag do banco para o modo empresa.
        """

        sql = """
        update ns.configuracoes set valor=0 where CAMPO = 1 AND APLICACAO = 0
        """

        self.db_adapter.execute(sql)

    def backup_conjuntos(self):
        """
        Cria tabelas para backup completo da estrautura de conjuntos do BD (os conjuntos em si,
        suas associações com os estabelecimentos e com os dados).
        """

        # Copiando tabelas de estrutura
        sqls = [
            'create table conjuntos_bkp as select * from ns.conjuntos;',
            'create table estabelecimentosconjuntos_bkp as select * from ns.estabelecimentosconjuntos;'
        ]

        for sql in sqls:
            try:
                self.db_adapter.execute(sql)
            except Exception as e:
                self.log_warning(f'Problema ao criar tabela de backup: {e}')

        # Tratando do owner destas tabelas
        try:
            sqls = [
                'alter table conjuntos_bkp owner to group_nasajon;'
                'alter table estabelecimentosconjuntos_bkp owner to group_nasajon;'
            ]

            for sql in sqls:
                self.db_adapter.execute(sql)
        except:
            pass

        # Copiando tabelas de cadastro
        for cadastro in ConverteModoEmpresaCommand.CADASTROS:
            tabela = ConverteModoEmpresaCommand.CADASTROS[cadastro]

            try:
                sql = f"create table {tabela}_bkp as select * from ns.{tabela};"
                self.db_adapter.execute(sql)
            except Exception as e:
                self.log_warning(f'Problema ao criar tabela de backup: {e}')

            # Tratando do owner da tabela
            try:
                sql = f"alter table {tabela}_bkp owner to group_nasajon;"
                self.db_adapter.execute(sql)
            except:
                pass

    def delete_conjuntos(self):
        """
        Exclui todos os conjuntos do BD (após backup realizado).

        Apaga tanto as associações com os dados, quanto os conjuntos em si, e suas associações com os estabelecimentos.
        """

        for cadastro in ConverteModoEmpresaCommand.CADASTROS:
            if cadastro == 13:
                # Pulando conjunto de rubricas
                continue

            tabela = ConverteModoEmpresaCommand.CADASTROS[cadastro]
            sql = f"truncate ns.{tabela};"
            self.db_adapter.execute(sql)

        sqls = [
            'delete from ns.estabelecimentosconjuntos where cadastro <> 13;',
            'delete from ns.conjuntos where cadastro <> 13;'
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)

    def list_grupos_empresariais(self):
        """
        Lista todos os grupos empresariais do BD.
        """

        sql = 'select codigo, grupoempresarial from ns.gruposempresariais'

        return self.db_adapter.execute_query(sql)

    def insert_novos_conjuntos(self, grupo_empresarial: Dict[str, Any]):
        """
        Cria novos conjuntos para um grupo empresarial, considerando todos os tipos de cadastro, com exceção do 13 (rubricas).
        """

        sql = 'INSERT INTO ns.conjuntos (conjunto, descricao, cadastro, codigo) VALUES (:id, :descricao, :cadastro, :codigo)'

        descricao = f"{grupo_empresarial['codigo']}{grupo_empresarial['codigo']}"

        ids_conjuntos = {}
        for cadastro in ConverteModoEmpresaCommand.CADASTROS:
            if cadastro == 13:
                # Pulando conjunto de rubricas
                continue

            id = uuid.uuid4()
            self.db_adapter.execute(
                sql, id=id, cadastro=cadastro, descricao=descricao, codigo=descricao)
            ids_conjuntos[cadastro] = id

        return ids_conjuntos

    def list_estabelecimentos_from_grupo(self, grupo_empresarial: Dict[str, Any]) -> List[uuid.UUID]:
        """
        Lista os ids dos estabelecimentos do grupo empresarial recebido.
        """

        sql = """
        select est.estabelecimento as id from ns.estabelecimentos as est
        join ns.empresas as emp on (emp.empresa = est.empresa)
        join ns.gruposempresariais as ge on (ge.grupoempresarial = emp.grupoempresarial and ge.grupoempresarial = :grupo_id)
        """

        return self.db_adapter.execute_query(sql, grupo_id=grupo_empresarial['grupoempresarial'])

    def insert_novas_associacoes_conjuntos_estabelecimentos(self, grupo_empresarial: Dict[str, Any], ids_conjuntos: Dict[int, uuid.UUID]):
        """
        Associa os estabelecimentos do grupo empresarial recebido, aos novos conjuntos criados.
        """

        estabelecimentos = self.list_estabelecimentos_from_grupo(
            grupo_empresarial)
        for estabelecimento in estabelecimentos:
            for cadastro in ids_conjuntos:
                sql = "insert into ns.estabelecimentosconjuntos (estabelecimento, conjunto, cadastro, permissao) values (:estabelecimento_id, :conjunto_id, :cadastro, true);"
                self.db_adapter.execute(
                    sql, estabelecimento_id=estabelecimento['id'], conjunto_id=ids_conjuntos[cadastro], cadastro=cadastro)

    def copy_permissoes_dados(self, grupo_empresarial: Dict[str, Any], ids_conjuntos: Dict[int, uuid.UUID]):
        """
        Copia, para cada tabela de relacionamento entre conjunto e dados, as antigas associações, porém trocando para os novos
        conjuntos criados para o mesmo grupo empresarial em questão.

        Parâmetros:
        grupo_empresarial: Dados do grupo empresarial sendo trabalhado
        ids_conjuntos: Dicionário, chaveado pelo número do cadastro e apontando para todos os novos
        ids de conjuntos criados para o tal grupo empresarial.
        """

        for cadastro in ids_conjuntos:
            tabela_conjunto = ConverteModoEmpresaCommand.CADASTROS[cadastro]
            sql = f"""
            insert into ns.{tabela_conjunto} (registro, conjunto)
            select distinct bkp.registro, (:conjunto)::uuid from {tabela_conjunto}_bkp as bkp
            join estabelecimentosconjuntos_bkp as ec_bkp on (bkp.conjunto = ec_bkp.conjunto)
            join ns.estabelecimentos as est on (est.estabelecimento = ec_bkp.estabelecimento)
            join ns.empresas as emp on (emp.empresa = est.empresa)
            where emp.grupoempresarial = :grupo_id
            """
            self.db_adapter.execute(
                sql, conjunto=ids_conjuntos[cadastro], grupo_id=grupo_empresarial['grupoempresarial'])

    def main(self, pars: List[str]):
        # self.config_logger()

        start_time = time.time()
        try:

            self.log('Iniciando conversão para o modo empresa')

            # Verificando se o BD já está em modo contábil
            if self.is_modo_empresa():
                raise Exception('Este banco já está em modo empresa.')

            # Ajustando as permissões do BD
            self.log('Ajustando permissoes do group nasajon')
            self.ajusta_persmissoes_group_nasajon()

            # Fazendo backup da estrutura de conjuntos:
            self.log('Copiando a estrutura de conjuntos')
            self.backup_conjuntos()

            # Apagando a estrutura de conjuntos (com exceção da parte de rubricas)
            self.log('Excluindo os conjuntos atuais')
            self.delete_conjuntos()

            # Tratando dos conjuntos para cada grupo empresarial
            for grupo_empresarial in self.list_grupos_empresariais():
                self.log(
                    f"Tratando o grupo empresarial {grupo_empresarial['codigo']}")

                # Criando os novos conjuntos do grupo empresarial
                self.log('Insrindo novos conjuntos')
                ids_conjuntos = self.insert_novos_conjuntos(grupo_empresarial)

                # Associando os novos conjuntos aos esabelecimentos do grupo
                self.log(
                    'Inserindo novas associações entre conjuntos e estabelecimentos')
                self.insert_novas_associacoes_conjuntos_estabelecimentos(
                    grupo_empresarial, ids_conjuntos)

                # Fazendo DE-PARA das permissões antigas (no backup), para os novos conjuntos:
                self.log('Copiando permissões dos dados')
                self.copy_permissoes_dados(grupo_empresarial, ids_conjuntos)

            # Atualizando a configuração para o modo empresa
            self.log('Alterando a flag de conjfiguração do modo de instalação')
            self.set_modo_empresa()

            self.log('Concluindo a conversão')
        finally:
            self.log("--- TEMPO TOTAL GERAL %s seconds ---" %
                     (time.time() - start_time))
