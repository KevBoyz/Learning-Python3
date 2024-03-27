from itertools import count
from builtins import list as b_list
from time import sleep
from contextlib import contextmanager



class Crazy:
    def __init__(self, l):
        self.list = l

    def __enter__(self):
        list = self.list  # Trolada master
        return list

    def __exit__(self, type, value, traceback):
        list = b_list



with Crazy([1,2,3]) as alist:
    alist.append(4)
    
print(list)


@contextmanager
def caneco():
    try:
        print('xpto')
        yield
    except Exception as error:
        print(error if error else None)
    finally:
        print('xpta')


with caneco():
    print('dentro do contexto')
