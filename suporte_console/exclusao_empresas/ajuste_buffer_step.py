from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict


class AjusteBufferStep(Step):
    """
    Responsavel por criar ou atualizar as tabelas "2" do buffer de exclusão,
    as quais são as que de fato a etapa de exclusão usa, e onde se garante a
    unicidade das chaves a excluir.
    """

    def list_entidades(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select distinct(schema_name) from exclusao.entidades where pk_name is not null
        """

        return self.db_adapter.execute_query(sql)

    def verifica_buffer2_exists(self, entidade: Dict[str, Any]):
        schema = entidade['schema_name']

        # Recuperando todas as entidades passiveis de exclusao
        sql = f"""
        select 1 from exclusao.{schema}2 limit 1
        """

        try:
            self.db_adapter.execute_query(sql)
            return True
        except Exception as e:
            return False

    def create_tabela_buffer2(self, entidade: Dict[str, Any]):
        schema = entidade['schema_name']

        sql = f"""
        create table exclusao.{schema}2 as select distinct * from exclusao.{schema};
        """
        self.db_adapter.execute(sql)

    def update_tabela_buffer2(self, entidade: Dict[str, Any]):
        schema = entidade['schema_name']

        sql = f"""
        insert into exclusao.{schema}2 (table_name, id, excluido)
        select distinct e.table_name, e.id, e.excluido from exclusao.{schema} as e
        left join exclusao.{schema}2 as e2 on (e.id=e2.id)
        where e2.id is null;
        """
        self.db_adapter.execute(sql)

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Ajustando tabelas de seleção (para haver unicidade nos registros)...')

        # Recuperando todas as entidades passiveis de exclusao
        entidades = self.list_entidades()

        # Criando ou atualizando tabela buffer2
        for entidade in entidades:
            if self.verifica_buffer2_exists(entidade):
                self.update_tabela_buffer2(entidade)
            else:
                self.create_tabela_buffer2(entidade)
