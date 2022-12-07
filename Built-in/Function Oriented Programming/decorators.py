from time import time, perf_counter
from math import trunc
from functools import wraps, lru_cache


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
        #print('function:', func.__name__)
        return(func(*args, **kwargs))
    return wrap


@debug
def f(x):
    return x**2


#print(f(5))


def timer2(n):  # Decorator args
    def decorator(func):  # Function
        @wraps(func)
        def wrap(*args, **kwargs):  # Func args
            times = []
            for c in range(0, n):
                start = time()
                func(*args, **kwargs)
                end = time()
                times.append(end-start)
                print(f'[{c+1}] {times[-1]:.2f} secs')
            return f'Median: {sum(times)/n:.2f}' # Time as median
        return wrap
    return decorator


@timer2(10)
#@lru_cache
def l(n):
    a = sum([n**10 for n in range(999999)])


#print(l(11))


class Demo:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(self.func.__name__)
        self.func()
        

@Demo
def lol():
    print('something')

lol()
