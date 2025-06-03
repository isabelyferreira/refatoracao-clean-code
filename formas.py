from abc import ABC, abstractmethod
import math


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio * self.raio


class FormaFactory:
    @staticmethod
    def criar_forma(tipo, *args):
        formas = {
            "quadrado": lambda: Quadrado(*args),
            "retangulo": lambda: Retangulo(*args),
            "circulo": lambda: Circulo(*args),
        }
        forma = formas.get(tipo.lower())
        if forma:
            return forma()
        raise ValueError(f"Forma '{tipo}' não é suportada.")


if __name__ == "__main__":
    formas = [
        FormaFactory.criar_forma('quadrado', 4),
        FormaFactory.criar_forma('retangulo', 4, 5),
        FormaFactory.criar_forma('circulo', 3),
    ]

    for forma in formas:
        print(f"Área: {forma.calcular_area():.2f}")