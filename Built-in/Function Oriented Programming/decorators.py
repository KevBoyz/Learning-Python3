from time import time
from math import trunc
from functools import wraps


def timer(func):
    def wrapper(_range):
        start = time()
        func(_range)
        end = time()
        print(trunc(end - start), 'seconds')
    return wrapper


@timer
def xpto(_range):  # Nested functions
    for x in range(0, _range):
        pass


#xpto(9 ** 8)


def debug(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print('function:', func.__name__)
        return(func(*args, **kwargs))
    return wrap


@debug
def f(x):
    return x**2


print(f(5))


def loop(n):  # Decorator args
    def decorator(func):  # Function
        def wrap(*args, **kwargs):  # Func args
            for c in range(0, n):
                func(*args, **kwargs)
        return wrap
    return decorator


@loop(3)
def l():
    print(1)


l()