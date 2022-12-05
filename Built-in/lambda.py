from functools import reduce
from operator import mul

print(list(map(lambda x: x*3, [2, 3, 4])))
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
print(reduce(lambda x, y: x+y, [30, 20, 50, 100]))

print((lambda x: x % 2 and 'odd' or 'even')(5))
print((lambda x: "Even" if x % 2 == 0 else "Odd")(3))

numbers = list(map(lambda x: x, [1, 2, 3, 4, 5, 6]))
odds = filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6])
for n in odds:
    numbers.remove(n)
print(numbers)


from itertools import takewhile

print(list(takewhile(lambda x: x <= 5, list(range(1, 11)))))
