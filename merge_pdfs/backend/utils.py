from functools import wraps


def not_implemented(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"{func.__name__} is not implemented yet!")

    return inner
