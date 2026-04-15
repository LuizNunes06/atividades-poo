class Animal():

    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f"O {self.nome} falou!"
    

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f"{self.nome} diz: Au Au!"
    
class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        return f"{self.nome} diz: Miau Miau!"
    
cachorro = Cachorro("Floquinho")
gato = Gato("Nina")

animais = [cachorro, gato]

for animal in animais:
    print(animal.falar())