class Carro():

    def __init__(self, marca, modelo, qtd_combustivel_energia):
        self.marca = marca
        self.modelo = modelo
        self.qtd_combustivel_energia = qtd_combustivel_energia

    def dirigir(self):
        pass

class CarroGasolina(Carro):

    def __init__(self, marca, modelo, qtd_combustivel_energia):
        super().__init__(marca, modelo, qtd_combustivel_energia)


    def dirigir(self):

        return f"O {self.modelo} está andando \nCombustível restante: {round(self.qtd_combustivel_energia, 2)}L \n"
    
class CarroEletrico(Carro):

    def __init__(self, marca, modelo, qtd_combustivel_energia):
        super().__init__(marca, modelo, qtd_combustivel_energia)
    
    def dirigir(self):
        return f"O {self.modelo} está andando \nBateria restante: {round(self.qtd_combustivel_energia, 2)}% \n"
    

carroGasolina = CarroGasolina("Renault", "Boreal", 40)
carroEletrico = CarroEletrico("BYD", "Seal", 80)

print(carroGasolina.dirigir())
print(carroEletrico.dirigir())