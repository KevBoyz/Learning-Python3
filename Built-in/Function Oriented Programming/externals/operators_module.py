import operator as o
from functools import reduce



#  print(reduce(lambda x, y: x + y, [1, 2 ,3, 4, 5]))  # Bad
print(reduce(o.add, [1, 2, 3, 4, 5]))  # Good

print(sorted(['xa', 'xb', 'xc'], key=lambda string: string[1]))
print(sorted(['xa', 'xb', 'xc'], key=o.itemgetter(1)))

print(o.attrgetter('__add__')(5)(5))  # 5.__add__(5)