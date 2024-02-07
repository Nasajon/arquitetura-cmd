from suporte_console.db_adapter2 import DBAdapter2
from typing import List


class HandlerUniques:
    def __init__(self, db_adapter: DBAdapter2, registros: List[str]) -> None:
        self.db_adapter = db_adapter
        self.registros = registros

    def criar_unique(self, schema: str, tabela: str, unique: str, colunas: List[str]) -> bool:
        cols = ','.join(colunas)

        # Verificando se a unique existe
        sql = f"""
        select 1
        from information_schema.constraint_column_usage 
        where
            table_schema = :schema
            and table_name = :tabela
            and constraint_name = :constraint_name
        """
        exists_constraint = self.db_adapter.execute_query(
            sql, schema=schema, tabela=tabela, constraint_name=unique)
        if len(exists_constraint) > 0:
            return True

        # Tentando criar a unique, se não existir
        try:
            sql = f"""
            alter table {schema}.{tabela} add constraint "{unique}" unique ({cols});
            """

            self.db_adapter.execute(sql)
            return True
        except:
            return False

    def criar_unique_registro(self, registro: str) -> bool:
        tabela = f'conjuntos{registro}'
        unique = f'uk_ns_{tabela}_conjunto_registro'
        return self.criar_unique('ns', tabela, unique, ['registro'])

    def criar_uniques(self):
        erros_criacao_fk = {}

        erros_criacao_fk['estabelecimento'] = self.criar_unique(
            'ns', 'estabelecimentosconjuntos', 'uk_ns_estabelecimentosconjuntos_estabelecimento_conjunto', ['estabelecimento', 'conjunto'])
        erro = self.criar_unique('ns', 'estabelecimentosconjuntos',
                                 'uk_ns_estabelecimentosconjuntos_estabelecimento_cadastro', ['estabelecimento', 'cadastro'])
        erros_criacao_fk['estabelecimento'] = erros_criacao_fk['estabelecimento'] or erro

        for registro in self.registros:
            erros_criacao_fk[registro] = self.criar_unique_registro(registro)

        return erros_criacao_fk
