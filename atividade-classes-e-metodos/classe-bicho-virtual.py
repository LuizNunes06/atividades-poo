class BichoVirtual:
    fome = 80
    saude = 100

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self, novaFome):
        self.fome = novaFome

    def alterarSaude(self, novaSaude):
        self.saude = novaSaude

    def alterarIdade(self, novaIdade):
        self.idade = novaIdade

    def listaInfoBichinho(self):
        headerTabela = f"{5*" "} Info. do {self.nome} {5*" "}"
        tamanhoLinha = len(headerTabela) + 2
        print(f"{'_' * tamanhoLinha} \n|{headerTabela}| \n{'-' * tamanhoLinha} \n| | ")


bichinho = BichoVirtual("Teste", 2)

bichinho.listaInfoBichinho()