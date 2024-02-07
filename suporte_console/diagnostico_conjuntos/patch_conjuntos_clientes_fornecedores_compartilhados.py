import uuid

from suporte_console.diagnostico_conjuntos.patch_conjuntos_participantes_compartilhados import PatchConjuntosParticipantesCompartilhados


class PatchConjuntosClientesFornecedoresCompartilhados(PatchConjuntosParticipantesCompartilhados):
    """
    Patch para resolver o problema de quando conjuntos de clientes ou fornecedores
    estejam indevidamente compartilhado por mais de uma empresa ou grupo empresarial
    (de acordo com o modo da instalação).
    """

    def can_execute(self, registro_tipo: str) -> bool:
        return registro_tipo == 'clientes' or registro_tipo == 'fornecedores'

    def get_estabelecimento_maior_uso(self, registro: str, id: uuid.UUID):
        sql = f"""
        with estabelecimentos as (
            select
                distinct ec.estabelecimento
            from
                ns.conjuntos{registro} as assoc
                join ns.estabelecimentosconjuntos as ec on (ec.conjunto = assoc.conjunto)
            where assoc.registro = :id
        ),
        docfis as (
            select
                df.id_estabelecimento as estabelecimento, count(*) as qtd
            from
                estabelecimentos as est
                join ns.df_docfis as df on (
                    est.estabelecimento = df.id_estabelecimento
                    and (df.id_destinatario = :id or df.id_remetente = :id)
                )
            group by df.id_estabelecimento
        ),
        titulos as (
            select
                tt.id_estabelecimento as estabelecimento, count(*) as qtd
            from
                estabelecimentos as est
                join financas.titulos as tt on (
                    est.estabelecimento = tt.id_estabelecimento
                    and tt.id_pessoa = :id
                )
            group by tt.id_estabelecimento
        ),
        qtd_estabelecimento as (
            select
                coalesce(df.estabelecimento, tt.estabelecimento) as estabelecimento,
                (coalesce(df.qtd, 0) + coalesce(tt.qtd, 0)) as qtd
            from
                docfis as df
                full outer join titulos as tt on (tt.estabelecimento = df.estabelecimento)
        )
        select estabelecimento from qtd_estabelecimento order by qtd desc limit 1
        """

        return self.db_adapter.execute_query_first_result(sql, id=id)

    def list_dados_ignorar(self, registro: str):
        sql = """
        select id from ns.pessoas where pessoa in ('PAG_NAOIDENTIFICADO', 'DEP_NAOIDENTIFICADO')
        """

        ignorados = self.db_adapter.execute_query(sql)

        return [i['id'] for i in ignorados]
