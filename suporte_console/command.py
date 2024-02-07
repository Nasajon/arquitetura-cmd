import datetime
import logging
import sys

from abc import ABC, abstractmethod
from typing import List

from suporte_console.db_adapter2 import DBAdapter2


class Command(ABC):

    db_adapter: DBAdapter2
    command_id: str

    def __init__(self, db_adapter: DBAdapter2, command_id: str = None) -> None:
        super().__init__()
        self.db_adapter = db_adapter
        self.command_id = command_id
        self.config_logger()

    def config_logger(self):
        # Configuring logger
        data = datetime.datetime.now()
        log_file_name = f"{self.command_id} - {data.year}-{data.month}-{data.day}-{data.hour}-{data.minute}.log"

        logger = logging.getLogger(self.command_id)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler(sys.stdout)
        file_handler = logging.FileHandler(log_file_name)

        console_format = logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s')
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_format)
        file_handler.setFormatter(file_format)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    def log(self, msg: str):
        logger = logging.getLogger(self.command_id)
        logger.info(msg)

    def log_debug(self, msg: str):
        logger = logging.getLogger(self.command_id)
        logger.debug(msg)

    def log_warning(self, msg: str):
        logger = logging.getLogger(self.command_id)
        logger.warning(msg)

    def log_exception(self, msg: str):
        logger = logging.getLogger(self.command_id)
        logger.exception(msg)

    @abstractmethod
    def main(self, pars: List[str]):
        pass
