from functools import reduce

print(list(map(lambda x: x*3, [2, 3, 4])))
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
print(reduce(lambda x, y: x+y, [30, 20, 50]))

print((lambda x: x % 2 and 'odd' or 'even')(5))
print((lambda x: "Even" if x % 2 == 0 else "Odd")(3))
