class Fila:
    c_fila = []

    @classmethod
    def c_entrar(cls, *obj):
        for e in obj:
            cls.c_fila.append(e)

    def __init__(self) -> None:
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        self.c_entrar(obj)  # cls is migrated to self (equivalent to self.c_fila.append(obj))


Fila().c_entrar(1,2,3,4,5)  # Monkey patch
f = Fila()  # Class with changes
f.s_entrar(1)
print(f.s_fila, f.c_fila)