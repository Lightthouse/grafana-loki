import logging
import logging_loki
import os

class LogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        return True

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
            'url': 'http://localhost:3100/loki/api/v1/push',
            'tags': {'application': 'grf'},
            'version': '2',
            # 'filter': ['loki_tags']
        }
    },

    'loggers': {
        'based': {
            'level': 'INFO',
            'handlers': ['loki'],
        }
    }
}