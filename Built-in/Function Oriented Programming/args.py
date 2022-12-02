def a(x):  # Positional arg
    ...


def b(x=1):  # Named arg
    ...


def c(*, x=2, y=3): # Explicit Named args
    print(x**y)  


def d(x=2, *, y=5):  # Hybrids <- * -> Required nameds
    print(x+y)



def e(x, /, y):  #  Required positionals <- / -> Hybrids
    print(x+y)


# Packing
def f(*args, **kwargs):  
    print(args)  # Positionals
    print(kwargs)  # Nameds

#f(1,2,3,4, a=1, b=2, c=4)


# Unpaking
def _min(a, b , c, *args):
    print(min(a, b, c))


def _max(a=0, b=0, c=0, **kwargs):
    print(max(a, b, c))


# _min(*(1, 2, 3), 4, 5, 6)  # Passing packs
# _max(**{'a': 1, 'b': 2, 'c': 3}, d=4, e=5, f=6)