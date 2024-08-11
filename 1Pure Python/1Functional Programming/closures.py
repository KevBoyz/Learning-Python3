import typing as tp
from numbers import Number


def cl_sum(n1:Number) -> tp.Callable:
    """
    Take and store one number on it's context
    """
    def sum(n2:Number) -> Number:
        """
        Return the sum of (external function number) + (passed number)
        """
        return n1 + n2
    return sum


sum2 = cl_sum(2)
print(sum2(2))



def sum_5(n1:Number) -> tp.Callable:
    """
    Take and store one number on it's context
    """
    def sum(n2:Number) -> Number:
        """
        Return the sum of (external function number) + (passed number)
        """
        nonlocal n1  # Changing the 
        n1 = 5  # free var value
        return n1 + n2
    return sum

sum5 = sum_5(10)
print(sum5(4))



def say_hello(salutation):  # Lambda clousure
    return lambda name: f'{salutation} {name}'

sh = say_hello('Hello')
print(sh('Kevin'))


"""def diga_oi(saudacao):  # Attr error
    def mudar_saudacao(nova_saudacao):
        nonlocal saudacao
        saudacao = nova_saudacao

    diga_oi.mudar_saudacao = mudar_saudacao
    return lambda nome: '{} {}'.format(saudacao, nome)

ahoy = diga_oi('Ahoy')
ahoy('Jaber') # 'Ahoy Jaber'
ahoy.mudar_saudacao('Olá')
ahoy('Jaber') # 'Olá Jaber'
"""

class Say_hello:  # Class that work as closure
    def __init__(self, saudacao) -> None:
        object.__setattr__(self, 'saudacao', saudacao) 

    def __setattr__(self, *ignored):
        raise NotImplemented

    def __call__(self, nome:str) -> str:
        return f'{self.saudacao} {nome}'


sh2 = Say_hello('Hello')
print(sh2('Kevin'))


# Making a decorator
def is_even(func):
    def warp(*args):
        r = func(*args)
        if r % 2 == 0:
            return True, r
        else:
            return False, r
    return warp

#  Explicit use
ev = is_even(lambda x, y: x + y)
print(ev(3, 5))


# Implict use
@is_even
def sum3(x, y):
    return x + y


print(sum3(4,5))
