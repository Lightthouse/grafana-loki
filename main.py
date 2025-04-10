import logging
import logging_loki
from config import logger_conf


# альтернативный url, если мы в общей сети docker
# url="http://loki:3100/loki/api/v1/push",


# Один из вариантов создания хендлера, но лучше использовать стандартный
handler = logging_loki.LokiHandler(
    url="http://localhost:3102/loki/api/v1/push",
    tags={"application": "my-app"},
    auth=None,
    version="2",
)

# Добавляем хендлер через метод
# logger.addHandler(handler)


# Создаём логгер
logging.config.dictConfig(logger_conf)
logger = logging.getLogger("based")


def main():
    print("Hello from grafana!")
    # Логируем ошибку
    logger.error(
        "Отправляем писульки",
        extra={"tags": {"service": "grafana app", 'test': 'wtf'}},
    )


if __name__ == "__main__":
    main()
