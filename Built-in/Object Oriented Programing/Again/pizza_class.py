class Pizza:
    pedaços = 8
    @classmethod
    def mudar_pedaçõs(cls, n):
        cls.pedaços = n

    @classmethod
    def mudar_preço(cls, p):
        cls.preço = p

    def pegar_pedaço(self):
        self.pedaços -= 1


class Mussarela(Pizza):
    preço = 15

    @staticmethod
    def ingredientes():
        return ['queijo', 'molho de tomate']

class Calabreza(Pizza):
    preço = 20

    @staticmethod
    def ingredientes():
        return ['calabreza', 'cebola']


class MeioAMeio(Pizza):
    def __init__(self, sabor1, sabor2) -> None:
        super().__init__()
        self.sabor1 = sabor1
        self.sabor2 = sabor2
        self.preço = (self.sabor1.preço + self.sabor2.preço) / 2

    def ingredientes(self):
        return self.sabor1.ingredientes() + self.sabor2.ingredientes()


ma = MeioAMeio(Mussarela, Calabreza)
print(ma.ingredientes())
