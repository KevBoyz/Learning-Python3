from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        print('undefined are moving')


class Human(Animal):
    def move(self):
        print('The human are moving')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} are running')


class Abc(Animal):
    def move(self):
        super().move()  # Calling the method of abstract with super()


hm = Human()
dg = Dog('Gabiru')
ts = Abc()

hm.move()
dg.move()
ts.move()