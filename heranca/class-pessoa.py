class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getPessoa(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \n\n")

class Funcionario(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumento(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)

    def getFuncionario(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nSalário: R${self.salario:.2f} \n\n")

pessoa = Pessoa("Luiz", 20)
funcionario = Funcionario("Isa", 18, 2500)
funcionario.aumento(10)

pessoa.getPessoa()
funcionario.getFuncionario()
