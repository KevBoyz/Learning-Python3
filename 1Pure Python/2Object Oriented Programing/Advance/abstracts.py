from abc import ABC, abstractmethod

class Fila(ABC):

    @abstractmethod
    def entrar():
        ...

    @abstractmethod
    def sair():
        ...
    
    @abstractmethod
    def __len__():
        ...

    @abstractmethod
    def __getitem__():
        ...
    
    @abstractmethod
    def __contains__():
        ...



class FilaDeSuperMercado(Fila):
    def __init__(self):
        self.fila = []

    def entrar(self, special=False):
        if special:   
            self.fila.insert(0, 'SpecialPerson')
        else:
            self.fila.append('Person')

    def sair(self, pos=0):
        self.fila.pop(pos)

    def __len__(self):
        return len(self.fila)

    def __getitem__(self, i):
        return self.fila[i]

    def __contains__(self, v):
        return v in self.fila

    def __str__(self) -> str:
        return f'{self.fila}'

    def __repr__(self) -> str:
        return f'FilaDeSuperMercado({self.fila})'

        
@Fila.register  # Set this class as a sub of Fila withough implement nothing
class FilaDeBanheiro:  # This say that class is Fila like
    ...  # insinstance(FilaDeBanheiro, Fila)  == True
    