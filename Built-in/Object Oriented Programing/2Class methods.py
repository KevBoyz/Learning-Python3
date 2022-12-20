from datetime import datetime
from random import randint


class Prototype:
    """I'm a doc string!"""
    year = int(datetime.now().year)  # Class variable, it's going be in all objects

    def __init__(self, name, age):  # This dunder method initialize the object
        self.name = name
        self.age = age

    def __str__(self):  # Dunder method
        return self.name

    def greeting(self):
        return f"Hello, I'm {self.name}! I have {self.age} years."

    def getYear(self):
        return self.year - self.age

    @classmethod
    def byBirth(cls, name, biy):           # Instance the object with her birth year
        return cls(name, cls.year - biy)

    @staticmethod
    def id_generator(x, y):           # Static method don't read the instance or class, is just a way
        return randint(x, y)          # to organize functions that relation to object


person = Prototype('Kevin', 14)
print(person.__doc__)  # Special method that references the docstring
print(person.__str__())  # Returns the informal form of object in string type
print(person.getYear())  # Returns the born year

person2 = Prototype.byBirth('Kevin', 2007)  # using classmethod
print(person2.greeting())

print(Prototype.id_generator(235, 1000))

# del person.name  # Delete the name attribute of the class
# del person  # Del class
