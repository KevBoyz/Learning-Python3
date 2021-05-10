class Person(object):
    def __new__(cls, name, age):  # Create new object and call __init__, **kwarg = key word arguments
        return object.__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        print(str(self))
        print(int(self.age + 0.9))

    def __str__(self):  # Return a impermeable version of class
        return f'|{self.name}_{str(self.age)}|'

    def __int__(self):  # Convert value to int
        return int(self)




obj = Person('Kevin', 14)
obj.test()