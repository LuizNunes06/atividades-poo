class Bola():
    def __init__(self, cor, circunferencia, material):

        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return f"A bola é {self.cor}"
    
bola = Bola("Azul", 10, "Borracha")


print(bola.mostraCor())

bola.trocaCor("Vermelha")

print(bola.mostraCor())