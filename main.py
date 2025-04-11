import logging
from config import logger_conf


# Создаём логгер
# logging.config.dictConfig(logger_conf)
# logger = logging.getLogger("based")
logger = logging.getLogger('root')


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
        logging.error('Последний заезд')


if __name__ == "__main__":
    start()
