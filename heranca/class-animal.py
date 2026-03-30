class Animal():
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def comer(self):
        self.peso += 1


class Cachorro(Animal):
    
    def latir(self):
        print("Au au au!!!")

class Gato(Animal):

    def miar(self):
        print("Miau miau")

cachorro = Cachorro("Floquinho", 20)
gato = Gato("Marrie", 5)

escolhaAnimal = int(input(f"Qual animal deseja alimentar? \n\n1- Cachorro.\n2- Gato.\n\nOpção escolhida: "))
escolhaAcao = int(input(f"O que deseja fazer com o animal? \n\n1- Alimentar.\n2- Fazer barulho.\n\nOpção escolhida: "))

while escolhaAnimal != 0 and escolhaAcao != 0:

    if escolhaAnimal == 1 and escolhaAcao == 1:
        cachorro.comer()
        print(f"O peso de {cachorro.nome} é: {cachorro.peso}kg")

    if escolhaAnimal == 1 and escolhaAcao == 2:
        cachorro.latir()

    if escolhaAnimal == 2 and escolhaAcao == 1:
        gato.comer()
        print(f"O peso de {gato.nome} é: {gato.peso}kg")

    if escolhaAnimal == 2 and escolhaAcao == 2:
        gato.miar()

    escolhaAnimal = int(input(f"Qual animal deseja alimentar? \n\n1- Cachorro.\n2- Gato.\n\nOpção escolhida: "))

    escolhaAcao = int(input(f"O que deseja fazer com o animal? \n\n1- Alimentar.\n2- Fazer barulho.\n\nOpção escolhida: "))