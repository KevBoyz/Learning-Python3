from time import time, sleep
from math import trunc


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


xpto(9 ** 6)
