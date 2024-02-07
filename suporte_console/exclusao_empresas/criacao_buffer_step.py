from suporte_console.exclusao_empresas.step import Step
from typing import Any, Dict


class CriacaoBufferStep(Step):
    """
    Cria as tabelas primárias de buffer para a exclusão, onde as etapas de
    seleção dos dados irão armazenar os IDs dos dados a excluir
    (porém ainda sem garantir a unicidade).
    """

    def list_entidades(self):
        # Recuperando todas as entidades passiveis de exclusao
        sql = """
        select distinct(schema_name) from exclusao.entidades where pk_name is not null
        """

        return self.db_adapter.execute_query(sql)

    def create_tabela_exclusao(self, entidade: Dict[str, Any]):
        schema = entidade['schema_name']

        # Apagando a tabela, se já existir
        sql = f"""
        drop table if exists exclusao.{schema}
        """
        self.db_adapter.execute(sql)

        # Criando a tabela em si
        sql = f"""
        create table exclusao.{schema} (
            table_name varchar(100) not null,
            id uuid not null,
            excluido boolean not null default false,
            excluindo boolean not null default false
        )
        """
        self.db_adapter.execute(sql)

        # Criando o índice na tabela
        sql = f"""
        create index on exclusao.{schema} (table_name, id, excluido)
        """
        self.db_adapter.execute(sql)

        # Criando outro índice na tabela
        # sql = f"""
        # create index on exclusao.{schema} (table_name, id)
        # """
        # db_adapter.execute(sql)

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Criando tabelas de buffer do processo de exclusão...')

        # Recuperando todas as entidades passiveis de exclusao
        entidades = self.list_entidades()

        # Analisando, para cada entidade, se o relacionamento precisa ser tratado
        for entidade in entidades:
            self.create_tabela_exclusao(entidade)
