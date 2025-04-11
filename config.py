import logging
import logging_loki
import os


# Добавляем в логи данные для фильтрации. Формат: tags: {'thread': 11}
class LogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):

        if not hasattr(record, 'tags'):
            record.tags = {}

        record.tags['function'] = record.funcName
        record.tags['line'] = record.lineno
        record.tags['file'] = record.filename
        return True


loki_url = os.getenv('LOKI_URL') + '/loki/api/v1/push'
application = os.getenv('APP_NAME')
service = os.getenv('SERVICE_NAME')

logger_conf = {
    'version': 1,
    'formatters': {
        'console_msg': {
            'format': '{levelname} {msg} {filename} {funcName} {lineno} {exc_info}',
            'style': '{'
        }
    },
    'filters': {
        'loki_tags': {
            '()': LogFilter
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'console_msg'
        },
        'loki': {
            'class': 'logging_loki.LokiHandler',
            'level': 'DEBUG',
            'formatter': 'console_msg',
            'url': loki_url,
            'tags': {'application': application, 'service': service},
            'version': '2',
            'filters': ['loki_tags']
        }
    },

    'loggers': {
        'based': {
            'level': 'INFO',
            'handlers': ['loki'],
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console']
        }
    }
}
