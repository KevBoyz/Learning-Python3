# Override

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return print(f'{self.name}: Hello!')


class Student(Person):
    def greeting(self):  # The method has overdid
        return print(f'{self.name}: Hello everyone!')




st = Student('Kevin')

st.greeting()
