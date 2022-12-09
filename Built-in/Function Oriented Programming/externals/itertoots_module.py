import itertools as it
from typing import NoReturn, Iterable, Any
from numbers import Number


# Infinite generators


def inf_counter(start:Number, step:Number=1) -> Iterable:
    """
    Retorna um contador que gera seu proximo valor com __next__().
    Args:
        - start: Valor inicial da contagem
        - step: Valor a ser somado por chamada [default=1]
    """
    return it.count(start, step)
    

def iter_cycler(i:Iterable) -> Iterable:
    """
    Percorre o iteravel até sua exaustão e então reinicia o ciclo.
    Args:
        - i: Iteravel qualquer
    """
    return it.cycle(i)


def repeater(obj:Any, times:int) -> Iterable:
    """
    Retorna um iterador que repete o objeto até a exaustão
    Args:
        - obj: Objeto qualquer
        - times: Quantidade totasl de vezes a repetir 
    """


# Combinatory generators


def cartesian_product(*i: Iterable, repeat:int=1) -> Iterable:
    """
    Retorna o produto cartesiano entre os iteradores passados
    Args:
        - i: 1 ou mais iteradores
        - repeat: Quantidade de repetições
    Ex:
        ([1,2], [3,4]) -> ([1,3], [1,4], [2,3], [2,4])

    """
    return it.product(i, repeat=repeat)


# print(list(it.product([1,2], repeat=2)))
# print(list(it.permutations([1,2,3])))
# print(list(it.combinations([1,2,3], 2)))  # wit replacment


# print(list(it.accumulate([1,2,3,4,5], lambda x, y: x*y)))
# filterfalse(predicate, iterable)

# print(list(it.chain.from_iterable([[1,2,3], [1,2,3]])))
# print(list(it.dropwhile(lambda x: x <= 5, [1,2,3,4,5,6,7,8])))
"""
data = [
("spaghetti", "10:23:52"), 
  ("spaghetti", "10:27:52"), 
  ("pennete_rigate", "11:14:44"), 
  ("pennete_rigate", "13:17:24"), 
  ("ravioli", "11:45:33"),   
  ("pizza", "19:45:44")
]
for key, value in it.groupby(data, lambda x: x[0]):
    print({key: list(value)})
"""