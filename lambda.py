from functools import reduce

'''
for simplificado:
print([x * 2 for x in numbers])

lambda arguments : expression

Uma função lambda pode receber qualquer número de argumentos, mas só pode ter uma expressão.

Em uma função lambda, declarações como return, pass, assert, ou raise irá levantar uma SyntaxError exceção

Estudar lambda em Python com map, reduce e filter

A map()função executa uma função especificada para cada item em um iterável.
O item é enviado para a função como parâmetro.

O construtor list () retorna uma lista em Python

reduce()é útil quando você precisa aplicar uma função a um iterável e reduzi-la a um único valor cumulativo
'''

s = lambda x, y: x * y
ss = (lambda x: x + 1)(6)

x = lambda a, b, c: a + b + c

hm = lambda x: x % 2 and 'odd' or 'even'
bt = lambda x: "Even" if x % 2 == 0 else "Odd"

age = lambda x: 'more than 18' if x>18 else 'less than 18'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair = list(filter(lambda x: x % 2 == 0, numbers))

sum = reduce(lambda a, b: a + b, numbers)

multiply = list(map(lambda x: x*2, numbers))

[print(n) for n in numbers] # for simplificado
