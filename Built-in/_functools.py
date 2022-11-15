import functools as fc


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

print(steps(7)) # 7 misses 6 hits
print(steps(4)) # 0 misses 1 hit
print(steps.cache_info())