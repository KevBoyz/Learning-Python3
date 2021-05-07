class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Wolf(Animal):
    def howl(self):
        return print(f'{self.name} are howling')


class Dog(Wolf):
    def bark(self):
        return print(f'{self.name} are barking')


dog = Dog('Gabiru', 1, 'Fem')

dog.howl()
dog.bark()