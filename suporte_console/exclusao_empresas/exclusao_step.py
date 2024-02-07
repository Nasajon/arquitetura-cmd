import logging
import time

from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict, List


class ExclusaoStep(Step):
    """
    Etapa que promove de fato a exclusão dos dados, utilizando as tabelas de
    buffer secundárias (com unicidade dos dados), como controle das exclusões
    (por meio da coluna booleana excluido).

    Essa etapa desativa triggers, apaga FKs, e apaga os dados (com delete direto,
    se forem "poucos" dados, ou criando uma tabela temporária com os dados a manter,
    fanzendo truncate na original, e depois restaurando os dados com insert select).
    """

    QTD_LIMITE_EXCLUSAO_DIRETA = 100000

    def excluir_casos_especiais(self):
        sql = f"""
        delete from scritta.sn_cfg where id_empresa in (
            select id from exclusao.ns2 where table_name='empresas'
        )
        """

        self.db_adapter.execute(sql)

    def limpar_casos_especiais_fk(self):
        sqls = [
            f"""
            update persona.trabalhadores set empresaanterior=null where empresaanterior in (
                select id from exclusao.ns2 where table_name='empresas'
            )
            """,
            f"""
            update persona.trabalhadores set trabalhadorempresaanterior=null where trabalhadorempresaanterior in (
                select trabalhador from persona.trabalhadores where empresa in (
                    select id from exclusao.ns2 where table_name='empresas'
                )
            )
            """,
            f"""
            update persona.trabalhadores set trabalhadorcontratoanterior=null where trabalhadorcontratoanterior in (
                select trabalhador from persona.trabalhadores where empresa in (
                    select id from exclusao.ns2 where table_name='empresas'
                )
            )
            """,
        ]

        for sql in sqls:
            self.db_adapter.execute(sql)

    def is_modo_empresa(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        SELECT VALOR as modo FROM NS.CONFIGURACOES WHERE CAMPO = 1 AND APLICACAO = 0
        """

        modo = self.db_adapter.execute_query_first_result(sql)

        if str(modo["modo"]) == "0":
            return True
        else:
            return False

    def list_entidades(self):
        # Verificando se está em modo contabil
        if self.is_modo_empresa():
            modo_contabil = False
        else:
            modo_contabil = True

        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select * from exclusao.entidades where pk_name is not null and (not apenas_modo_contabil or :modo_contabil)
        """

        return self.db_adapter.execute_query(sql, modo_contabil=modo_contabil)

    def desliga_triggers(self):
        sql = """
        SET session_replication_role = replica;
        """

        self.db_adapter.execute(sql)

    def liga_triggers(self):
        sql = """
        SET session_replication_role = DEFAULT;
        """

        self.db_adapter.execute(sql)

    def conta_tabela_excluir(self, entidade: Dict[str, Any]):
        sql = f"""
        select count(*) as qtd from {entidade['schema_name']}.{entidade['table_name']}
        """

        return self.db_adapter.execute_query_first_result(
            sql, table={entidade["table_name"]}
        )["qtd"]

    def conta_itens_excluir(self, entidade: Dict[str, Any]):
        sql = f"""
        select count(*) as qtd from exclusao.{entidade['schema_name']}2
        where table_name = :table and not excluido
        """

        return self.db_adapter.execute_query_first_result(
            sql, table={entidade["table_name"]}
        )["qtd"]

    def excluir_itens_diretamente(self, entidade: Dict[str, Any]):
        sql = f"""
        delete from
            {entidade['schema_name']}.{entidade['table_name']} as td
        using
            exclusao.{entidade['schema_name']}2 as te
        where
            te.table_name = :table
            and te.id = td.{entidade['pk_name']}
            and not te.excluido
        """

        self.db_adapter.execute(sql, table={entidade["table_name"]})

    def limpar_fks_estabelecimentos_usuarios(self, fk_name: str):
        sql = f"""
        with estabelecimentos_excluir as (
            select id from exclusao.ns2
            where table_name='estabelecimentos'
            and not excluido
        )
        update
            ns.usuarios
        set
            {fk_name} = null
        where
            {fk_name} in (select id from estabelecimentos_excluir)
        """

        self.db_adapter.execute(sql)

    def limpar_fks_empresas_usuarios(self, fk_name: str):
        sql = f"""
        with empresas_excluir as (
            select id from exclusao.ns2
            where table_name='empresas'
            and not excluido
        )
        update
            ns.usuarios
        set
            {fk_name} = null
        where
            {fk_name} in (select id from empresas_excluir)
        """

        self.db_adapter.execute(sql)

    def copiar_dados(self, entidade: Dict[str, Any]):
        sql = f"""
        create table exclusao.temp as select td.* from
        {entidade['schema_name']}.{entidade['table_name']} as td
        left join exclusao.{entidade['schema_name']}2 as te on (
            te.table_name = :table
            and te.id = td.{entidade['pk_name']}
            and not te.excluido
        ) where te.id is null
        """

        self.db_adapter.execute(sql, table={entidade["table_name"]})

    def marca_excluidos(self, entidade: Dict[str, Any]):
        sql = f"""
        update exclusao.{entidade['schema_name']}2
        set excluido = true
        where table_name = :table
        and not excluido
        """

        self.db_adapter.execute(sql, table={entidade["table_name"]})

    def excluir_tabela_temp(self):
        sql = """
        drop table if exists exclusao.temp
        """

        self.db_adapter.execute(sql)

    def limpa_tabela_origem(self, entidade: Dict[str, Any]):
        sql = f"""
        truncate table {entidade['schema_name']}.{entidade['table_name']};
        """

        self.db_adapter.execute(sql)

    def restaura_tabela_origem(self, entidade: Dict[str, Any]):
        sql = f"""
        INSERT INTO {entidade['schema_name']}.{entidade['table_name']} TABLE exclusao.temp
        """

        self.db_adapter.execute(sql)

    def get_scripts_create_fks(self, entidade: Dict[str, Any]):
        sql = f"""
        SELECT 'ALTER TABLE '||nspname||'."'||relname||'" ADD CONSTRAINT "'||conname||'" '|| pg_get_constraintdef(pg_constraint.oid) || ';' as script
        FROM pg_constraint
        INNER JOIN pg_class ON conrelid=pg_class.oid
        INNER JOIN pg_namespace ON pg_namespace.oid=pg_class.relnamespace
        where
            nspname != 'pg_catalog'
            and contype='f'
            and pg_get_constraintdef(pg_constraint.oid)::varchar ilike '%REFERENCES {entidade['schema_name']}.{entidade['table_name']}%'
        """

        return self.db_adapter.execute_query(sql)

    def execute_scripts_create_fks(self, scritps: List[Dict[str, Any]]):
        for script in scritps:
            try:
                self.db_adapter.execute(script["script"])
            except Exception as e:
                self.log(str(e))

    def drop_fks(self, entidade: Dict[str, Any]):
        sql = f"""
        SELECT nspname as schema_name, relname as table_name, conname as constraint_name
        FROM pg_constraint
        INNER JOIN pg_class ON conrelid=pg_class.oid
        INNER JOIN pg_namespace ON pg_namespace.oid=pg_class.relnamespace
        where
            nspname != 'pg_catalog'
            and contype='f'
            and pg_get_constraintdef(pg_constraint.oid)::varchar ilike '%REFERENCES {entidade['schema_name']}.{entidade['table_name']}%'
        """

        fks = self.db_adapter.execute_query(sql)

        for fk in fks:
            sql = f"""
            ALTER TABLE {fk['schema_name']}."{fk['table_name']}" DROP CONSTRAINT "{fk['constraint_name']}"
            """

            self.db_adapter.execute(sql)

    def escreve_log_fks(self, fks: List[str]):
        logger = logging.getLogger("log_fks")
        for fk in fks:
            logger.info(fk["script"])

    def main(self, data: str, invert_selecao: bool):
        self.log("Iniciando exclusão real dos dados...")

        scripts_create_fks = []

        try:
            self.desliga_triggers()

            start_time = time.time()

            self.log("Limpando FKs Usuarios...")
            self.limpar_fks_estabelecimentos_usuarios("ultimoestabelecimentocontabil")
            self.limpar_fks_estabelecimentos_usuarios("ultimoestabelecimentopersonaweb")
            self.limpar_fks_estabelecimentos_usuarios("ultimaempresascritta")
            self.limpar_fks_empresas_usuarios("ultimaempresapersona")
            self.log("--- %s seconds ---" % (time.time() - start_time))

            self.log("Excluindo casos especiais...")
            self.excluir_casos_especiais()
            self.log("--- %s seconds ---" % (time.time() - start_time))

            self.log("Limpando casos especiais de FK...")
            self.limpar_casos_especiais_fk()
            self.log("--- %s seconds ---" % (time.time() - start_time))

            # Recuperando todas as entidades passiveis de exclusao
            entidades = self.list_entidades()

            # Iterando as entidades
            for entidade in entidades:
                start_time = time.time()

                self.log("")
                self.log(
                    f"INICIANDO ENTIDADE {entidade['schema_name']}.{entidade['table_name']}"
                )

                self.log("Excluindo a tabela temporária...")
                self.excluir_tabela_temp()
                self.log("--- %s seconds ---" % (time.time() - start_time))

                self.log("Recuperando a quantidade de linhas a excluir...")
                qtd_linhas = self.conta_itens_excluir(entidade)
                self.log("--- %s seconds ---" % (time.time() - start_time))

                if qtd_linhas <= 0:
                    self.log("Nada a excluir. Pulando a entidade.")
                    continue

                # print('Recuperando a quantidade de linhas na tabela a excluir...')
                # qtd_linhas_tabela = conta_tabela_excluir(db_adapter, entidade)
                # print("--- %s seconds ---" % (time.time() - start_time))

                self.log("Guardando os scripts para recriar as FKs...")
                scripts_create_fks_novos = self.get_scripts_create_fks(entidade)
                self.escreve_log_fks(scripts_create_fks_novos)
                scripts_create_fks += scripts_create_fks_novos
                self.log("--- %s seconds ---" % (time.time() - start_time))

                # if qtd_linhas <= QTD_LIMITE_EXCLUSAO_DIRETA and qtd_linhas_tabela <= QTD_LIMITE_TABELA_EXCLUSAO:
                if qtd_linhas <= ExclusaoStep.QTD_LIMITE_EXCLUSAO_DIRETA:
                    self.log("Removendo as FKs...")
                    self.drop_fks(entidade)
                    self.log("--- %s seconds ---" % (time.time() - start_time))

                    self.log("Excluindo os dados diretamente...")
                    self.excluir_itens_diretamente(entidade)
                    self.log("--- %s seconds ---" % (time.time() - start_time))
                else:
                    self.log("Copiando dados a manter...")
                    self.copiar_dados(entidade)
                    self.log("--- %s seconds ---" % (time.time() - start_time))

                    self.log("Removendo as FKs...")
                    self.drop_fks(entidade)
                    self.log("--- %s seconds ---" % (time.time() - start_time))

                    self.log("Limpando a tabela de origem...")
                    self.limpa_tabela_origem(entidade)
                    self.log("--- %s seconds ---" % (time.time() - start_time))

                    self.log("Restaurando dados a manter...")
                    self.restaura_tabela_origem(entidade)
                    self.log("--- %s seconds ---" % (time.time() - start_time))

                self.log("Marcando dados excluidos...")
                self.marca_excluidos(entidade)
                self.log("--- %s seconds ---" % (time.time() - start_time))

            self.log("Excluindo a última tabela temporária...")
            self.excluir_tabela_temp()

            self.log("RECRIANDO AS FKs...")
            start_time = time.time()
            self.execute_scripts_create_fks(scripts_create_fks)
            self.log("--- %s seconds ---" % (time.time() - start_time))

        finally:
            self.liga_triggers()
