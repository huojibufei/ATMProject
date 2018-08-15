from core import src
import logging.config
from conf import settings

def auth(func):
    def inner(*args,**kwargs):
        if src.user_info['name']:
            res = func(*args,**kwargs)
            return res
        else:
            src.login()
    return inner


def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger


