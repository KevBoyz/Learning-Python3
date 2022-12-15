class Jogador:
    def __init__(self, camisa) -> None:
        self.camisa = camisa

class Pássaro:
    def __init__(self, nome) -> None:
        self.nome = nome

class CanarinhoPistola(Pássaro, Jogador):
    def __init__(self, nome, camisa) -> None:
        Pássaro.__init__(nome)
        Jogador.__init__(camisa)