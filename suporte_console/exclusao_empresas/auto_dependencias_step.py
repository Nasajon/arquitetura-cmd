from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict


class AutoDependenciasStep(Step):
    """
    Passo oicional capaz de popular a tabela exclusao.entidades_dependencias
    com as FKs que estiverem faltando (retiradas da modelagem do BD).
    """

    def list_entidades(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select * from exclusao.entidades where pk_name is not null
        """

        return self.db_adapter.execute_query(sql)

    def list_fk_references(self, entidade: Dict[str, Any]):
        # Recuperando todas as fks que apontam para uma entidade
        sql = """
        select * from util.list_fk_references(:schema, :table, :pk)
        """

        return self.db_adapter.execute_query(sql, schema=entidade['schema_name'], table=entidade['table_name'], pk=entidade['pk_name'])

    def verifica_dependencia_entidade(self, entidade: Dict[str, Any], fk_ref: Dict[str, Any]):
        # Recuperando todas as fks que apontam para uma entidade
        sql = """
        select 1 from exclusao.entidades_dependencias
        where
            schema_name_origem = :schema_origem
            and table_name_origem = :table_origem
            and schema_name_destino = :schema_destino
            and table_name_destino = :table_destino
            and fk_column = :column
        """

        return self.db_adapter.execute_query(
            sql,
            schema_origem=fk_ref['schema'], table_origem=fk_ref['table'],
            schema_destino=entidade['schema_name'], table_destino=entidade['table_name'],
            column=fk_ref['column']
        )

    def insert_dependencia_entidade(self, entidade: Dict[str, Any], fk_ref: Dict[str, Any]):
        # Recuperando todas as fks que apontam para uma entidade
        sql = """
        insert into exclusao.entidades_dependencias (
            schema_name_origem, table_name_origem,
            schema_name_destino, table_name_destino,
            fk_column
        ) values (
            :schema_origem, :table_origem,
            :schema_destino, :table_destino,
            :column
        )
        """

        return self.db_adapter.execute(
            sql,
            schema_origem=fk_ref['schema'], table_origem=fk_ref['table'],
            schema_destino=entidade['schema_name'], table_destino=entidade['table_name'],
            column=fk_ref['column']
        )

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Inserindo FKs faltantes, na tabela de controle das dependencias...')

        # Recuperando todas as entidades passiveis de exclusao
        entidades = self.list_entidades()

        # Analisando, para cada entidade, se o relacionamento precisa ser tratado
        for entidade in entidades:
            fk_refs = self.list_fk_references(entidade)

            for fk in fk_refs:
                # Verificando se a dependencia já existe
                dependencias_recuperadas = self.verifica_dependencia_entidade(
                    entidade, fk)

                if len(dependencias_recuperadas) <= 0:
                    # Inserindo cada dependência entre as entidades
                    self.insert_dependencia_entidade(entidade, fk)
