from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict


class PermissoesNasajonStep(Step):
    """
    Aplica permissões para o group_nasajon, para a estrutura que permanecerá no BD,
    após o processo de exclusão.
    """

    def list_entidades(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select distinct(schema_name) from exclusao.entidades where pk_name is not null
        """

        return self.db_adapter.execute_query(sql)

    def alter_owner(self, entidade: Dict[str, Any]):
        schema = entidade['schema_name']

        sql = f"""
        alter table exclusao.{schema}2 owner to group_nasajon;

        """
        self.db_adapter.execute(sql)

    def alter_owner_tabelas_controle(self):
        sql = f"""
        alter table exclusao.entidades owner to group_nasajon;
        alter table exclusao.entidades_dependencias owner to group_nasajon;
        """
        self.db_adapter.execute(sql)

    def grant_on_schema(self):
        sql = f"""
        GRANT ALL ON SCHEMA exclusao TO group_nasajon;
        """
        self.db_adapter.execute(sql)

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Aplicando permissões para o group_nasajon (para a estrutura que ficará no BD)...')

        # Recuperando todas as entidades passiveis de exclusao
        entidades = self.list_entidades()

        # Dando as permissões ao group_nasajon
        for entidade in entidades:
            self.alter_owner(entidade)

        self.alter_owner_tabelas_controle()

        self.grant_on_schema()
