import time
import uuid

from typing import Any, Dict, List

from suporte_console.command import Command


class UnificaConjuntosFornecedoresCommand(Command):
    """
    Este comando remove todos os conjuntos de fornecedores do banco de dados, independentemente do modo de instalação (empresa, ou escritório contábil).

    Em seguida, ele cria um único conjunto de fornecedores, associando o mesmo a todos os estabelecimentos, e, por fim, adicionar todos os fornecedores nesse único conjunto.

    A ideia do script é fazer com que os registros de fornecedores sejam compartilhados por todos os grupos empresariais contidos no banco de dados.
    """

    CADASTRO_CONJUNTO_FICHA = 5
    CADASTRO_CONJUNTO_FORNECEDOR = 7

    def ajusta_persmissoes_group_nasajon(self):
        """
        Roda a função ns.permissoes, para ajustar as permissões do BD.
        """

        try:
            sql = f"select * from ns.permissoes()"
            self.db_adapter.execute(sql)
        except Exception as e:
            self.log_warning(f"Erro manipulando permissões do BD clonado: {e}")

    def apaga_associacoes_conjuntos_fornecedores(self):
        """
        Remover todas as associações entre os fornecedores e os conjuntos.
        """

        sql = f"delete from ns.conjuntosfornecedores"
        self.db_adapter.execute(sql)

    def apaga_conjuntos_fornecedores(self):
        """
        Remover todos conjuntos de fornecedores.
        """

        sqls = [
            f"delete from ns.estabelecimentosconjuntos where cadastro=:cadastro",
            f"delete from ns.conjuntos where cadastro=:cadastro",
        ]

        for sql in sqls:
            self.db_adapter.execute(
                sql,
                cadastro=UnificaConjuntosFornecedoresCommand.CADASTRO_CONJUNTO_FORNECEDOR,
            )

    def insert_novo_conjunto_fornecedores(self) -> uuid.UUID:
        """
        Cria um novo conjunto de fornecedores que valerá para todos os grupos empresariais do banco de dados.
        """

        sql = "INSERT INTO ns.conjuntos (conjunto, descricao, cadastro, codigo) VALUES (:id, :descricao, :cadastro, :codigo)"

        descricao = f"GLOBAL_FORNECEDORES"

        id = uuid.uuid4()
        self.db_adapter.execute(
            sql,
            id=id,
            cadastro=UnificaConjuntosFornecedoresCommand.CADASTRO_CONJUNTO_FORNECEDOR,
            descricao=descricao,
            codigo=descricao,
        )

        return id

    def insere_associacao_estabelecimentos_conjunto_fornecedor(
        self,
        id_conjunto_fornecedor: uuid.UUID,
    ):
        """
        Insere as associações entre os estabelecimentos e o conjunto global de fornecedores.
        """

        sql = """
        insert into ns.estabelecimentosconjuntos (estabelecimento, conjunto, cadastro, permissao)
        select estabelecimento, :conjunto_fornecedor, :cadastro, true from ns.estabelecimentos
        """

        self.db_adapter.execute(
            sql,
            conjunto_fornecedor=id_conjunto_fornecedor,
            cadastro=UnificaConjuntosFornecedoresCommand.CADASTRO_CONJUNTO_FORNECEDOR,
        )

    def insere_associacao_registros_conjunto_fornecedor(
        self,
        id_conjunto_fornecedor: uuid.UUID,
    ):
        """
        Insere as associações entre os fornecedores contidos no BD, e o conjunto global de fornecedores.
        """

        sql = f"""
        insert into ns.conjuntosfornecedores (registro, conjunto)
        select id, :conjunto_fornecedor from ns.pessoas where fornecedorativado=1
        """

        self.db_adapter.execute(
            sql,
            conjunto_fornecedor=id_conjunto_fornecedor,
        )

    # def apaga_associacoes_fornecedores_fichas(self):
    #     """
    #     Remover todas as associações dos fornecedores como fichas no BD:
    #     """

    #     sqls = [
    #         f"delete from ns.conjuntosfichas where cadastro in (select id from ns.pessoas where fornecedorativado=1)",
    #     ]

    #     for sql in sqls:
    #         self.db_adapter.execute(
    #             sql,
    #             cadastro=UnificaConjuntosFornecedoresCommand.CADASTRO_CONJUNTO_FORNECEDOR,
    #         )

    # def insere_associacao_registros_conjunto_fichas(self):
    #     """
    #     Insere as associações entre os fornecedores contidos no BD, e cada conjunto ficha.
    #     """

    #     sql = f"""
    #     insert into ns.conjuntosfichas (registro, conjunto)
    #     select p.id, c.conjunto from
    #         ns.pessoas as p
    #         join ns.conjuntos as c on (
    #             c.cadastro=:cadastro
    #             p.fornecedorativado=1
    #         )
    #     """

    #     self.db_adapter.execute(
    #         sql,
    #         cadastro=UnificaConjuntosFornecedoresCommand.CADASTRO_CONJUNTO_FICHA,
    #     )

    def main(self, pars: List[str]):
        # self.config_logger()

        start_time = time.time()
        try:
            self.log("Iniciando unificação dos conjuntos de fornecedores")

            self.log("Ajustando permissoes do group nasajon")
            self.ajusta_persmissoes_group_nasajon()

            self.log(
                "Removendo todas as associações entre os fornecedores e os conjuntos."
            )
            self.apaga_associacoes_conjuntos_fornecedores()

            self.log("Removendo todos conjuntos de fornecedores.")
            self.apaga_conjuntos_fornecedores()

            self.log(
                "Criando um novo conjunto de fornecedores que valerá para todos os grupos empresariais do banco de dados."
            )
            id_conjunto_fornecedor = self.insert_novo_conjunto_fornecedores()

            self.log(
                "Inserindo as associações entre os estabelecimentos e o conjunto global de fornecedores."
            )
            self.insere_associacao_estabelecimentos_conjunto_fornecedor(
                id_conjunto_fornecedor
            )

            self.log(
                "Inserindo as associações entre os fornecedores contidos no BD, e o conjunto global de fornecedores."
            )
            self.insere_associacao_registros_conjunto_fornecedor(id_conjunto_fornecedor)

            self.log("Concluindo a unificação dos conjuntos de fornecedores.")
        finally:
            self.log(
                "--- TEMPO TOTAL GERAL %s seconds ---" % (time.time() - start_time)
            )
