class Two:
    v = 2
    def __add__(self, val):
        return self.v + val


# print(Two() + 2)


class Num:
    def __init__(self, v) -> None:
        self.v = v
    def __pos__(self):
        return Num(+self.v)  # Return new instance
    def __neg__(self):
        return Num(-self.v)
    def __add__(self, val):
        return Num(self.v + val)
    def __radd__(self, val):
        return Num(self.v + val)
    
    def __str__(self) -> str:
        return str(self.v)


# print(-Num(5) + 2 + 3)


class Mystr:
    def __init__(self, s) -> None:
        self.s = s
    def __neg__(self):
        return Mystr(self.s[::-1])
    def __str__(self):
        return self.s 


# print(-Mystr('String'))


class CoolList(list):
    def __add__(self, v):
        return CoolList([x + v for x in self])
    def __lshift__(self, v):
        self.append(v)
    def __rshift__(self, p=0):
        self.pop(p)    
    def __neg__(self):
        return reversed(self)


cl = CoolList()
cl << 1
cl << 2
print(cl + 2)
