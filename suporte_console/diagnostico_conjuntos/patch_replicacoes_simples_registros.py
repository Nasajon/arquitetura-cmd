import logging

from suporte_console.db_adapter2 import DBAdapter2


class PatchReplicacoesSimplesRegistros:
    def __init__(self, db_adapter: DBAdapter2) -> None:
        self.db_adapter = db_adapter

    def can_execute(self, registro_tipo: str) -> bool:
        return registro_tipo != 'estabelecimento'

    def execute(self, registro_tipo: str):
        """
        A restratégia aqui é:
        1. Criar uma tabela temporária, que guardará os dados replicados (resolvendo já as replicas)
        2. Remover os dados replicados da respectiva tabela de conjuntos
        3. Restaurar os dados para a tabela original, mas sem as replicas
        4. Apagar a tabela temporária
        """

        # Getting logger
        logger = logging.getLogger('diagnostico_conjuntos')

        logger.info('Excluindo tabela temporária dos registros replicados')
        self.excluir_tabela_temporaria_registros_replicados()

        logger.info('Criando tabela temporária dos registros replicados')
        self.cria_tabela_temporaria_registros_replicados(registro_tipo)

        logger.info('Excluindo associação com réplicas')
        self.excluir_registros_replicados(registro_tipo)

        logger.info('Restaurando associações, agora sem as réplicas')
        self.restaurar_registros_sem_replicas(registro_tipo)

        logger.info('Excluindo tabela temporária dos registros replicados')
        self.excluir_tabela_temporaria_registros_replicados()

    def cria_tabela_temporaria_registros_replicados(self, registro: str):
        sql = f"""
        create table temp_buffer_registros_replicados as 
        select registro, conjunto from ns.conjuntos{registro} group by registro, conjunto having count(*) > 1
        """

        return self.db_adapter.execute(sql)

    def excluir_registros_replicados(self, registro: str):
        sql = f"""
        delete from ns.conjuntos{registro}
        using temp_buffer_registros_replicados as b
        where b.registro = ns.conjuntos{registro}.registro and b.conjunto = ns.conjuntos{registro}.conjunto
        """

        return self.db_adapter.execute(sql)

    def restaurar_registros_sem_replicas(self, registro: str):
        sql = f"""
        insert into ns.conjuntos{registro} (registro, conjunto)
        select registro, conjunto from temp_buffer_registros_replicados
        """

        return self.db_adapter.execute(sql)

    def excluir_tabela_temporaria_registros_replicados(self):
        sql = f"""
        drop table if exists temp_buffer_registros_replicados
        """

        return self.db_adapter.execute(sql)
