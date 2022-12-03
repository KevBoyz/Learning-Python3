from itertools import *

def m(x, y):
    for c in range(x, y):
        yield x * y


l = [m(5, 10)]