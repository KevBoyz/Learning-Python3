import functools as fc
import operator as o


sum2 = fc.partial(o.add, 2)
mul2 = fc.partial(o.mul, 2)

all_sum = fc.partial(fc.reduce, o.add) 
#print(all_sum([1, 2, 3]))  # print(fc.reduce(lambda x,y: x+y, [1,2,3,4]))

all_mul = fc.partial(fc.reduce, o.mul)
#print(all_mul([5, 5]))

mulmap = fc.partial(map, mul2)
#print(list(mulmap([5, 2, 3])))

def exp(x, y):
    ...
   # print(x ** y)

exp2 = fc.partial(exp, y=2)
exp2(5)


class Xn:
    def __init__(self, color):
        self.color = color

    def change_color(self, color):
        self.color = color

    set_blue = fc.partialmethod(change_color, 'blue')

xn = Xn('white')
xn.set_blue()
# print(xn.color)


@fc.lru_cache  # https://realpython.com/lru-cache-python/
def steps(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return (
            steps(n - 3)
            +   steps(n - 2)
            +   steps(n - 1)
        )

#print(steps(7)) # 7 misses 6 hits
#print(steps(4)) # 0 misses 1 hit
#print(steps.cache_info())

class Xpto:
    @fc.cached_property  # Result will be cached and 
    def l(self):         # generated once time. 
        return list(range(0, 100))


import timeit
def time_me(number_of_times):
    def decorator(func):
        @fc.wraps(func)
        def wraps(*args, **kwargs):
            r = timeit.timeit(func, number=number_of_times)
            print(r/number_of_times)
        return wraps
    return decorator

@time_me(10)
def function():
    return 2*2


function()
