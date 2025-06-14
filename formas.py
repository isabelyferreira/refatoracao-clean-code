
import math

class Forma:
    def calcular_area(self):
        raise NotImplementedError("Método não implementado")

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
        if tipo == 'quadrado':
            return Quadrado(*args)
        elif tipo == 'retangulo':
            return Retangulo(*args)
        elif tipo == 'circulo':
            return Circulo(*args)
        else:
            raise ValueError(f"Tipo de forma '{tipo}' não é válido")

# Exemplos de uso
if __name__ == "__main__":
    formas = [
        FormaFactory.criar_forma('quadrado', 4),
        FormaFactory.criar_forma('retangulo', 4, 5),
        FormaFactory.criar_forma('circulo', 3)
    ]

    for forma in formas:
        print(f"Área: {forma.calcular_area():.2f}")
