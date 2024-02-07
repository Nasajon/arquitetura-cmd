from suporte_console.exclusao_empresas.step import Step


class PopularPKsStep(Step):
    """
    Popula as PKs faltantes na tabela de controle exclusao.entidades
    """

    def popula_pks_nulas(self):
        # Apagando a tabela, se já existir
        sql = f"""
        with todas_pks as (
            select
                (regexp_split_to_array(conrelid::regclass::varchar, '\.'))[1] AS schema_name,
                (regexp_split_to_array(conrelid::regclass::varchar, '\.'))[2] AS table_name,
                conname AS pk_constraint_name, 
                replace(replace(pg_get_constraintdef(oid)::varchar, 'PRIMARY KEY (', ''), ')', '') as column_name
            from
                pg_constraint 
            where
                contype = 'p' 
            order by
                conrelid::regclass::text, contype DESC
        )
        update
            exclusao.entidades as et
        set
            pk_name = tpks.column_name
        from
            todas_pks as tpks
        where
            tpks.schema_name = et.schema_name
            and tpks.table_name = et.table_name
            and et.pk_name is null;
        """
        self.db_adapter.execute(sql)

    def main(self, data: str, invert_selecao: bool):
        self.log(
            'Populando as PKs faltantes na tabela de controle exclusao.entidades...')
        self.popula_pks_nulas()
