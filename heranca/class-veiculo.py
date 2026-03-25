class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def getVeiculo(self):
        return f"Marca: {self.marca}\n Modelo: {self.modelo}\n Ano: {self.ano}"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def getCarro(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPortas: {self.portas}\n"
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def getMoto(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCilindradas: {self.cilindradas}\n"
    
carro = Carro("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CB500", 2019, 500)

print(carro.getCarro())
print(moto.getMoto())