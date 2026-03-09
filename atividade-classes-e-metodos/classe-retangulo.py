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
        return f"Área: {self.ladoA * self.ladoB}"

    def calculaPerimetro(self):
        return f"Perímetro: {self.ladoA * 2 + self.ladoB * 2}"
    
# Rodar com ctrl + F5

retangulo = Retangulo(input("Informe o lado A: "), input("Informe o lado B: "))

print(retangulo.retornarLados())
