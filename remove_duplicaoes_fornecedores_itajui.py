from suporte_console.database_config import create_pool
from suporte_console.db_adapter2 import DBAdapter2


FKS = [
    ("financas", "administradoreslegais", "responsavelpf"),
    ("financas", "administradoreslegais", "responsavelpj"),
    ("financas", "benspatrimoniaisproprietarios", "proprietario_participante_id"),
    ("financas", "centroscustoslancamentosexternos", "pessoa"),
    ("financas", "chequescustodias", "id_cliente"),
    ("financas", "clientesenviadosserasa", "id_cliente"),
    ("financas", "clienteslotesfaturas", "id_pessoa"),
    ("financas", "configuracoesterceirizacao", "id_fornecedor"),
    ("financas", "contas", "id_pessoa_emprestimo"),
    ("financas", "contasfornecedores", "id_fornecedor"),
    ("financas", "contratos", "detentor_id"),
    ("financas", "contratos", "fiador"),
    ("financas", "contratos", "participante"),
    ("financas", "contratos", "participantecomissao"),
    ("financas", "contratosclientespartilhas", "participante"),
    ("financas", "contratosorcamentospagar", "participante"),
    ("financas", "contratosvendedores", "participante"),
    ("financas", "despesasmedicas", "prestador"),
    ("financas", "faturas", "cliente"),
    ("financas", "inadimplenciasexcecoesclientes", "id_cliente"),
    ("financas", "itenscobrancas", "participante"),
    ("financas", "lancamentoscontas", "participante"),
    ("financas", "pix", "idpessoa"),
    ("financas", "prestacoesdecontas", "id_fornecedor"),
    ("financas", "previsoespagar", "participante"),
    ("financas", "previsoesreceber", "participante"),
    ("financas", "projetos", "cliente_id"),
    ("financas", "projetosclientes", "cliente_id"),
    ("financas", "projetosfornecedores", "fornecedor_id"),
    ("financas", "projetosvendedores", "vendedor_id"),
    ("financas", "rateiospadraorestricoes", "pessoa"),
    ("financas", "reembolsos", "id_pessoa"),
    ("financas", "reembolsospessoas", "pessoa"),
    ("financas", "renegociacoescontratos", "id_cliente"),
    ("financas", "renegociacoestitulos", "pessoa"),
    ("financas", "retencoestitulosreceber", "participante"),
    ("financas", "terceirizacaocobrancas", "id_fornecedor"),
    ("financas", "titulos", "id_pessoa"),
    ("financas", "titulos", "id_pessoa_reembolso"),
    ("financas", "tituloscancelados", "id_pessoa"),
    ("financas", "tituloscancelados", "id_pessoa_reembolso"),
    ("financas", "titulosreceberporvendedores", "participante"),
    ("financas", "vendedoresparticipacaocomissao", "pessoa"),
    ("financas", "vendedoresrenegociacoestitulos", "vendedor"),
]


def desliga_triggers(db: DBAdapter2):
    sql = """
    SET session_replication_role = replica;
    """

    db.execute(sql)


def liga_triggers(db: DBAdapter2):
    sql = """
    SET session_replication_role = DEFAULT;
    """

    db.execute(sql)


# TODO Trocar abaixo os dados de comunicação com o banco da Itajuí
db_pool = create_pool(
    "postgres",
    "postgres",
    "localhost",
    "5432",
    "itajui2",
    1,
)
with db_pool.connect() as conn:
    db = DBAdapter2(conn)

    try:
        desliga_triggers(db)

        sql = "select cnpj from ns.pessoas where fornecedorativado=1 and bloqueado=false and cnpj is not null group by cnpj having count(*)>1"

        fornecedores = db.execute_query(sql)

        for fornecedor in fornecedores:
            sql = "select id from ns.pessoas where fornecedorativado=1 and cnpj=:cnpj"
            repetidos = db.execute_query(sql, cnpj=fornecedor["cnpj"])
            ids_repetidos = [r["id"] for r in repetidos]
            id_ficar = ids_repetidos[0]
            ids_repetidos = ids_repetidos[1:]
            ids_repetidos_str = [str(id) for id in ids_repetidos]
            ids_repetidos_tuple = tuple(ids_repetidos)

            # Refazendo os apontamentos
            for fk in FKS:
                query = f"update {fk[0]}.{fk[1]} set {fk[2]}=:id_ficar where {fk[2]} in :ids_repetidos"
                print(query, id_ficar, ids_repetidos_str)
                print("\n")
                db.execute(query, id_ficar=id_ficar, ids_repetidos=ids_repetidos_tuple)

            # Apagando as repeticoes:
            queries_apaga_repeticoes = [
                "delete from ns.conjuntosfornecedores where registro in :ids_repetidos",
                "update ns.pessoas set bloqueado=true where id in :ids_repetidos",
            ]

            for query in queries_apaga_repeticoes:
                db.execute(query, ids_repetidos=ids_repetidos_tuple)
    finally:
        liga_triggers(db)
