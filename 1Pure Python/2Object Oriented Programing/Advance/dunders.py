class MyClass:
    def __new__(cls):
        print('Building')
        return super().__new__(cls)  # OBJECT __new__

    def __init__(self) -> None:
        print('Initialzing')
    def __del__(self):
        print('Finalyzing')


m = MyClass()
del m