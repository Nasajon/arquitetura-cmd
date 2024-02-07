import logging
import uuid

from suporte_console.db_adapter2 import DBAdapter2


class PatchReplicacoesSimplesEstabelecimentosConjuntos:
    def __init__(self, db_adapter: DBAdapter2) -> None:
        self.db_adapter = db_adapter

    def can_execute(self, registro_tipo: str) -> bool:
        return registro_tipo == 'estabelecimento'

    def execute(self, registro_tipo: str):
        """
        A restratégia aqui é:
        1. Recuperar os estabelecimentosconjuntos replicados (já resolvendo as réplicas pelo group by)
        2. Remover os dados replicados da tabela estabelecimentosconjuntos
        3. Inserir novamente, sem replicações, na tabela estabelecimentosconjuntos
        """

        # Getting logger
        logger = logging.getLogger('diagnostico_conjuntos')

        logger.info('Recuperando estabelecimentosconjuntos replicados')
        replicados = self.get_estabelecimentos_conjuntos_replicados()

        logger.info('Tratando as réplicas')
        for replica in replicados:
            self.excluir_estabelecimento_conjunto(
                replica['estabelecimento'], replica['conjunto'], replica['cadastro'])

            self.inserir_estabelecimento_conjunto(
                replica['estabelecimento'], replica['conjunto'], replica['cadastro'])

    def get_estabelecimentos_conjuntos_replicados(self):
        sql = """
        select estabelecimento, conjunto, cadastro from ns.estabelecimentosconjuntos
        group by estabelecimento, conjunto, cadastro having count(*) > 1
        """

        return self.db_adapter.execute_query(sql)

    def excluir_estabelecimento_conjunto(self, estabelecimento: uuid.UUID, conjunto: uuid.UUID, cadastro: int):
        sql = """
        delete from ns.estabelecimentosconjuntos where
            estabelecimento = :estabelecimento
            and conjunto = :conjunto
            and cadastro = :cadastro
        """

        return self.db_adapter.execute(sql, estabelecimento=estabelecimento, conjunto=conjunto, cadastro=cadastro)

    def inserir_estabelecimento_conjunto(self, estabelecimento: uuid.UUID, conjunto: uuid.UUID, cadastro: int):
        sql = """
        insert into ns.estabelecimentosconjuntos (estabelecimento, conjunto, cadastro, permissao)
        values (:estabelecimento, :conjunto, :cadastro, true);
        """

        return self.db_adapter.execute(sql, estabelecimento=estabelecimento, conjunto=conjunto, cadastro=cadastro)
