# Class attr approach

class AgeDescriptor:
    def __set__(self, obj, val):
        obj._age = val  # Try remove the _. This is no more a convension.

    def __get__(self, obj, objtype=None):
        return obj._age


class Client:

    age = AgeDescriptor()  # Descriptor instance

    def __init__(self, age) -> None:
        self.age = age  # Calls __set__

    def __str__(self):
        return f'{self.age}'  # Calls __get__

    
c = Client(10)
print(c)


# __init__ approach

class AgeDescriptor2:
    def __init__(self, age):
        self._age = age

    def __set__(self, obj, val):
        self._age = val  # Try remove the _. This is no more a convension.

    def __get__(self, obj, objtype=None):
        return self._age

    def __delete__(self):
        del self._age


class Client2:

    def __init__(self, age) -> None:
        self.age = AgeDescriptor2(age)  # Calls __set__

    def __str__(self):
        return f'{self.age}'  # Calls __get__

    
c = Client(10)
print(c)