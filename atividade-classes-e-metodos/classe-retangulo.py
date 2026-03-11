import math

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novoA, novoB):
        self.ladoA = novoA
        self.ladoB = novoB

    def retornarLados(self):
        return f"Lado A: {self.ladoA}\nLado B: {self.ladoB}"

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calculaPerimetro(self):
        return self.ladoA * 2 + self.ladoB * 2


# Rodar com ctrl + F5

area = Retangulo(
    float(input("Informe o lado A (em metros): ")),
    float(input("Informe o lado B (em metros): ")),
)

print(area.retornarLados())

pisos = Retangulo(
    float(input("Informe o comprimento do piso (em metros): ")),
    float(input("Informe a largura do piso (em metros): ")),
)

print(pisos.retornarLados())

rodape = Retangulo(
    float(input("Informe a altura do rodapé (em metros): ")),
    area.calculaPerimetro(),
)

pisosArea = area.calcularArea() / pisos.calcularArea()
pisosRodape = (rodape.ladoA * rodape.ladoB) / pisos.calcularArea()


print(
    f"Pisos necessários para cobrir {area.calcularArea()}m²: {pisosArea} \nPisos necessários para os rodapés: {pisosRodape} \nTotal de pisos necessários: {int(math.ceil(pisosRodape + pisosArea))}"
)
