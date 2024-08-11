from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    @abstractmethod
    def speak(self, thing):
        pass

    @abstractmethod
    def eat(self, food):
        pass

    @abstractmethod
    def walk(self, place):
        pass

    @abstractmethod
    def sleep(self, place):
        pass


class Gamer(Person):
    def __init__(self, name, age, game):
        self.game = game
        super().__init__(name, age)

    def speak(self, thing):
        print(f'{self.name} are speaking about {thing}')

    def eat(self, food):
        print(f'{self.name} are eating {food}')

    def walk(self, place):
        print(f'{self.name} are walking in {place}')

    def sleep(self, place):
        print(f'{self.name} are sleeping in {place}')

    def play(self):
        print(f'{self.name} are playing {self.game}')


gamer = Gamer('Kevin', 14, 'Alien Isolation')

gamer.speak('games')
gamer.walk('street')
gamer.eat('pudim')
gamer.sleep('the bed')

gamer.play()