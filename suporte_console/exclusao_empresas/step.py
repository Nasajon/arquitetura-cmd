import logging

from abc import ABC, abstractmethod
from xmlrpc.client import boolean
from suporte_console.db_adapter2 import DBAdapter2


class Step(ABC):

    db_adapter: DBAdapter2

    def __init__(self, db_adapter: DBAdapter2) -> None:
        super().__init__()
        self.db_adapter = db_adapter

    def log(self, msg: str):
        logger = logging.getLogger('exclusao_empresas')
        logger.info(msg)

    @abstractmethod
    def main(self, data: str, invert_selecao: boolean):
        pass
