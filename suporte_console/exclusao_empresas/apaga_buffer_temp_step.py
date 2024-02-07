from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict


class ApagaBufferTempStep(Step):
    """
    Apaga as tabelas de buffer primárias da exclusão (onde não é garantida a unicidade).
    """

    def list_entidades(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select distinct(schema_name) from exclusao.entidades where pk_name is not null
        """

        return self.db_adapter.execute_query(sql)

    def apagar_tabela_buffer_temp(self, entidade: Dict[str, Any]):
        schema = entidade['schema_name']

        sql = f"""
        drop table if exists exclusao.{schema}
        """
        self.db_adapter.execute(sql)

    def excluir_tabela_temp(self):
        sql = """
        drop table if exists exclusao.temp
        """

        self.db_adapter.execute(sql)

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Apagando tabelas de buffer do processo de exclusão...')

        # Recuperando todas as entidades passiveis de exclusao
        entidades = self.list_entidades()

        # Apagando as tabelas temporárias de buffer, das entidades
        for entidade in entidades:
            self.apagar_tabela_buffer_temp(entidade)

        # Apagando a tabela de copia dos dados a manter
        self.excluir_tabela_temp()
