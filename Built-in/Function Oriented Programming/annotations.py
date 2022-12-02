# libs: mypy, monkeytype

def f(x:int=0) -> int:
    return x * 2


def g(y:int, x:int) -> int:
    return y ** x


print(f.__annotations__)
print(g.__annotations__)



from numbers import Number
from typing import Union, Any, List, Dict, Sequence, NewType, Callable

Somavel = Union[Number, str]  # Union = one or other
Radian = NewType('Radiano', int)  #  int mean that this new type is a extencion of it
# Strings são somaveis por que possuem metodo __add__


def z(x: Somavel, y: Somavel) -> Somavel:
    return x + y  

print(z.__annotations__)


def any(x: Any):
    return x


def convert(x: List[Number]) -> int:
    return int(sum(x))


def new_account(name:str, age:int) -> Dict[str, Union[str, int]]:
    return {'name': name, 'age': age}  # Dict[keys, values]



calc: Dict[str, Callable] = {
    'sum': lambda x, y: x + y,
    'sub': lambda x, y: x - y
}

