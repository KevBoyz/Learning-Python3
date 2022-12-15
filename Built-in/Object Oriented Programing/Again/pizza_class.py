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



class Pizzaria:
    def __init__(self) -> None:
        self._forno = Forno()  # Encapsing 
        self._pizzaiolo = Pizzaolo()

    def pedido(self, pizza):
        pizza_pronta = self._pizzaiolo.preparar(pizza)
        print('Aqui está sua Pizza:', pizza_pronta)

    
class Forno:
    def __init__(self) -> None:
        self.lenha = 0
        self.pizzas = []

    def ligar(self):
        if self.lenha == None:
            raise 'NãoHáLenha'
        else:
            self.lenha -= 1 # Assando

    def desligar(self):
        ...


class Pizzaolo:
    def __init__(self):
        self.forno = Forno()

    def preparar(self, pizza):
        massa = []
        for i in pizza.ingredientes():
            massa.append(i)
        return self.assar(massa)

    def assar(self, massa):
        # Coloca no forno
        try:
            self.forno.ligar()
        except:
            self.forno.lenha += 1
            self.forno.ligar()
        self.forno.desligar()
        return self.tirar(massa)

    def tirar(self, pizza_pronta):
        return pizza_pronta
            