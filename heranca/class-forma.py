import math


class Forma:

    def __init__(self, nome):
        self.nome = nome

    def area(self):
        pass

    def __str__(self):
        return self.nome


class Retangulo(Forma):

    def __init__(self, comprimento, largura):
        super().__init__("Retângulo")
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        print(f"Área: {self.comprimento * self.largura}")

class Circulo(Forma):

    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def area(self):
        print(f"Área: {round( math.pi * self.raio ** 2, 2)}")

retangulo = Retangulo(5, 3)
circulo = Circulo(4)

print(retangulo)
retangulo.area()

print(circulo)
circulo.area()
