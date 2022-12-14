# built in high order functions

# lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]
# print(max(lista, key=sum))  # Same for min()


"""with open(r'file.txt') as f:
     for line in iter(f.readline, ''):
        print(line)"""

# print(sorted(['ab', 'bc', 'ad'], key=lambda x: x[1], reverse=True))

#print(list(filter(lambda x: x%2 == 0, [1,2,3,4,5])))

from functools import partial


def tail(iterable, n, key=None):
    if key:
        return key(iterable[-n:])
    else:
        return iterable[-n:]


print(list(tail([1,2,3,4,5], 3, key=partial(map, lambda x: x**2))))
