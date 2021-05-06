from datetime import datetime

# https://www.youtube.com/watch?v=RLVbB91A5-8

# A classe é um molde para criar objetos

# Classe simples

"""
class User:
    def speak(self):  # Funções em classes se tornam métodos
        print('The person is speaking...')


user = User()  # Criando objeto a partir de classe
user.speak()  # Utilizando o mtd speak e passando user como argumento
"""


# Classe como deve ser

class User:
    year = datetime.now().year # Atributos da classe são aplicadas a todos os objetos

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name  # Variáveis recebendo como valor os parâmetros
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def eat(self, food):
        if self.eating:
            print(f'{self.name} already eating')

    def by_year_of_birth(cls, year, year_of_birth):
        idade = cls.year - year_of_birth



user1 = User('Kevin', 14, False)
user2 = User('Pedro', 15, True)


          # Métodos de classes

# Métodos de instância

#  user.eat('Pizza')
#  print(f'Kevin birth in {user.year_of_birth()}')

