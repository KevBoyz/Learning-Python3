# Funções nativas da propria linguagem

list1 = [True, True, True]
list2 = [False, False, True]

# print(sum([5, 5, 10]))  # soma valores agrupados
# print(abs(1 - 12))  # retorna o valor absoluto de um número
# print(type(1.1))  # retorna o tipo do objeto

# print(all(list1))  # retorna True se todos os valores de um conjunto forem verdadeiros
# print(any(list2))  # retorna True se qualquer valor de um conjunto for True

# print(divmod(5, 2))  # retorna a divisão solucionada (dividendo, divisor)

'''
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False                            
  else:                
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
'''

# x = isinstance(5, int)  # retorna True se o objeto especificado for do tipo especificado
# x = isinstance("Hello", (float, int, str, list, dict, tuple)) # Varios tipos podem ser repassados
# Se hello for qualquer um dos tipos especificados retorna True

# print(round(5.76543, 2))  # Arredonda um valor float, sintaxe: round(number, digits)

# print(list(zip(list1, list2)))  # Une elementos de mesmo index

# zl = zip(list1,list2)  # Zip
# print(list(zip(*zl)))  # unZip
