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