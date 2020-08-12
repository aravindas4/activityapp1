import os
from .base import *

INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [  # noqa: F405
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = '127.0.0.1'


DEBUG_LOG_FILE = os.path.join(BASE_DIR, "../log/access.log")  # noqa: F405


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',  # noqa
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{DEBUG_LOG_FILE}',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
