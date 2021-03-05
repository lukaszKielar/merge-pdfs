import logging
from functools import wraps

logger = logging.getLogger(__name__)


def not_implemented(func):
    @wraps(func)
    def inner(*args, **kwargs):
        logger.warning("%s is not implemented yet!", func.__name__)

    return inner
