import logging
from config import logger_conf


# Создаём логгер
logging.config.dictConfig(logger_conf)
logger = logging.getLogger("based")


class Math:
    def calc(self, a: int, b: int):
        return a + b


class TwoMath(Math):
    @classmethod
    def calc(cls, a: int):
        return a / 0


def start():
    print("Поднялись")

    try:
        TwoMath.calc(11)

    except Exception as e:
        logger.error('Последний заезд')


if __name__ == "__main__":
    start()
