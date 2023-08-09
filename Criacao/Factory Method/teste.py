from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def movimentar(self) -> None: pass


class AnimalFactory(ABC):
    def __init__(self, especie) -> None:
        self.especie = self.get_especie(especie)
    
    @staticmethod
    def get_especie(tipo: str) -> Animal:
        if tipo == 'sapo':
            return Anfibio(tipo)
        if tipo == 'rato':
            return Roedor(tipo)
        assert 0, 'Animal não existe'

    def movimentar(self) -> None:
        self.especie.movimentar()

class Anfibio(Animal):
    def movimentar(self) -> None:
        print(f"{self.nome} está se movimentando")

class Roedor(Animal):
    def movimentar(self) -> None:
        print(f"{self.nome} está se movimentando")

if __name__ == "__main__":
    sapo = AnimalFactory("sapo")
    sapo.movimentar()

    rato = AnimalFactory("rato")
    rato.movimentar()


