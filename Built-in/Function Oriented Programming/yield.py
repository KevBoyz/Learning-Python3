from contextlib import contextmanager
import sys

v = False
# range(0, 100)  # generator function example


def print_all(iterator, v=False):
    if v:
        for val in iterator:
            print(val)


def the_next_function():  # Generate line-per-life of a file that is a generator
    with open('lambda.py', 'r') as file:
        for i in range(0, 5):
            print(file.__next__())


def generator_function():  # Iterable object, not simple data
    print('before 1') if v else None
    yield 1
    print('before 2') if v else None
    yield 2
    print('before 3') if v else None
    yield 3


# print(generator_function)  # Generator Function
# print(generator_function())  # Generator Object
generator = generator_function()
for value in generator_function():  # Consumes all yield
    print(value) if v else None


def test():
    while True:  # yield has no previous, it just goes ahead
        try:
            print(next(generator))  # netx item
        except StopIteration:
            print('No more items to generate: StopInteraction exception')
            break


def even_generator():
    while True:
        n = 1
        while True:
            yield n
            n += 2


even = even_generator()
# print(next(even))
# print(even.__next__())
# print(even.__next__())

print_all(even) if v else None


def chapters_sub_generator():
    yield 1.1
    yield 1.2


def chapters_generator():
    yield 1
    yield from chapters_sub_generator()  # yield from other yield
    yield 2


sequence = chapters_generator()
print_all(sequence)


def my_range(max_value):  # Custom range
    for val in range(max_value):
        yield val  # yield from [0, 1, 2, 3] or yield from range(max_value)
        if val == 5:
            return 'it\'s 5'  # Break clause -> StopInteraction with the return value -> Exception: it's 5


_range = my_range(10)
print_all(_range)


def gen_exp():
    yield from (n for n in range(0, 10) if n % 2 == 1)  # Even numbers exp


print_all(gen_exp())


@contextmanager
def context():
    print('Context initialized')
    yield
    print('Context finished')


# with context() as func:
#    print('Inside the context')


def coroutine(op1=False, op2=True):
    print('Coro initialized') if v else None
    while True:
        val = yield
        if op1:
            yield from (x*10 for x in val)
        elif op2:
            yield from val
        return 'All values generated'


c = coroutine()
c.__next__()  # Is necessary initialize the coroutine
# print(c.send('Kev Boyz'))  # if op1: c.send([1, 2, 3, 4]) -> 10, 20, 30, 40
print_all(c)


def id_gen(_range):
    for i in range(999999, _range, 99999999 * 2):
        yield i ** 9


for id in id_gen(99 ** 9999):
    print(id / 1, sys.getsizeof(id))
