class Cfunc:  # Methods working as functions
    def __init__(self, n:int) -> None:
        self.n = n

    def __call__(self, *args: int) -> int:
        return sum(args) * self.n

func = Cfunc(2)
print(func(1, 2, 3, 4, 5))
