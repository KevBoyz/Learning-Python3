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