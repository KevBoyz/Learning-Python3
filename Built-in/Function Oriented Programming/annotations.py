def f(x:int=0) -> int:
    return x * 2


def g(y:'number', x:'exp') -> 'n**exp':
    return y ** x


print(f.__annotations__)
print(g.__annotations__)
