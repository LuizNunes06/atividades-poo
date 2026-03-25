class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getPessoa(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \n\n")

class Estudante(Pessoa):

    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota

    def getEstudante(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nNota: {self.nota} \n\n")

pessoa = Pessoa("Luiz", 20)
estudante = Estudante("Isa", 18, 9)

pessoa.getPessoa()
estudante.getEstudante()
