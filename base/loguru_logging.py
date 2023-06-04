import logging
from loguru import logger


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def func(message):
    return logger.debug(message)

if __name__ == "__main__":
    func()