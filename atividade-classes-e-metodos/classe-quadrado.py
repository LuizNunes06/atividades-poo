class Quadrado():

    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, novoLado):
        self.lado = novoLado

    def retornaLado(self):
        return f"O tamanho do lado do quadrado é: {self.lado}"
    
    def calculaArea(self):
        return f"A área do quadrado é: {self.lado**2}"

quadrado = Quadrado(5)

print(quadrado.retornaLado())
print(quadrado.calculaArea())

print(quadrado.mudaLado(4))

print(quadrado.retornaLado())
print(quadrado.calculaArea())
