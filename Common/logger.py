import logging
from typing import Optional

class Logger:
    def __init__(self, name: Optional[str] = None):
        self.logger = logging.getLogger(name if name else "CommonLogger")
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(name)s: %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def debug(self, message: str):
        self.logger.debug(message) 