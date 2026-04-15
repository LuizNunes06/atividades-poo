class Animal():

    def __init__(self, nome = "animal"):
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
        return f"{self.nome} diz: Miau!"
    
class Peixe(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f"{self.nome} diz: Blub Blub!"
    
cachorro = Cachorro("Floquinho")
gato = Gato("Nina")
peixe = Peixe("Nemo")

print(cachorro.falar())
print(gato.falar())
print(peixe.falar())