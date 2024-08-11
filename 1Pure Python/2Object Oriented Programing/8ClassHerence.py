class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello! My name is {self.name}, I have {self.age} years old")


class Student(Person):  # Student class Herd the 'Person'
    def say_goodBye(self):
        print(f'- {self.name}: You known the rules and so do I. Say good Bye.')


st1 = Student('Kevin', 14)
st1.greeting()
st1.say_goodBye()


# Polymorphism

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return print(f'{self.name}: Hello!')


class Student(Person):
    def greeting(self):  # override
        return print(f'{self.name}: Hello everyone!')


st = Student('Kevin')

st.greeting()


# Multiple herence


class A:
    def a(self):
        print('worked')


class B:
    def b(self):
        print('worked too')


class C(A, B):
    def c(self):
        print('Ok, all working')


c = C()

c.a()
c.b()
c.c()


# Init foda


class Jogador:
    def __init__(self, camisa) -> None:
        self.camisa = camisa

class Camelo:
    def __init__(self, nome) -> None:
        self.nome = nome

class CanarinhoPistola(Camelo, Jogador):
    def __init__(self, nome, camisa) -> None:
        Camelo.__init__(nome)
        Jogador.__init__(camisa)
