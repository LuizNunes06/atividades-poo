import math


class Forma:

    def __init__(self, nome="forma"):

        self.nome = nome

    def area(self):
        pass


class Circulo(Forma):

    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2


class Quadrado(Forma):

    def __init__(self, lado):
        super().__init__("Quadrado")
        self.lado = lado

    def area(self):
        return self.lado**2


circulo = Circulo(5)
quadrado = Quadrado(4)

for forma in (circulo, quadrado):
    print(f"A área do {forma.nome} é: {round(forma.area(), 2)}")
