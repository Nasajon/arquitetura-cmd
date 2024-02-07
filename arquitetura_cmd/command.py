# import datetime
import logging

# import sys

from abc import ABC, abstractmethod
from typing import List

# from arquitetura_cmd.db_adapter2 import DBAdapter2


class Command(ABC):

    # db_adapter: DBAdapter2
    command_id: str

    def __init__(
        self,
        # db_adapter: DBAdapter2,
        command_id: str = None,
    ) -> None:
        super().__init__()
        # self.db_adapter = db_adapter
        self.command_id = command_id
        self.config_logger()

    def config_logger(self):
        logger = logging.getLogger("arquitetura_cmd")
        self.logger = logger

    def log(self, msg: str):
        self.logger.info(msg)

    def log_debug(self, msg: str):
        self.logger.debug(msg)

    def log_warning(self, msg: str):
        self.logger.warning(msg)

    def log_exception(self, msg: str):
        self.logger.exception(msg)

    @abstractmethod
    def main(self, pars: List[str]):
        pass
