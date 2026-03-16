class ContaCorrente:

    def __init__(self, numeroConta, nome, saldo=0):
        self.numeroConta = numeroConta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nome = novoNome

        print(
            f"\n|-------------- Mudança no nome --------------|\nNovo nome: {self.nome}"
        )

    def depositar(self, valorEntrada):
        self.saldo += valorEntrada
        print(
            f"\n|-------------- Deposito feito --------------|\nValor do depósito: {valorEntrada}\nNovo saldo: {self.saldo}"
        )

    def saque(self, valorSaida):
        if self.saldo >= valorSaida:
            self.saldo -= valorSaida
            
            print(
                f"\n|-------------- Saque feito --------------|\nValor do saque: {valorSaida}\nNovo saldo: {self.saldo}"
            )

        else:
            print(f"!!! Saldo insuficiente !!!\nSaldo na conta: R${self.saldo}")


contaCorrente = ContaCorrente(
    input("Informe o número da conta: "),
    input("Informe o nome: "),
)

escolha = int(
    input(
        f"O que será feito com a conta {contaCorrente.numeroConta}? \n\n1- Alterar o nome.\n2- Depositar.\n3- Sacar. \n4- Dados da conta \n0- Encerrar programa.\n\nOpção escolhida: "
    )
)

while escolha != 0:

    if escolha == 1:
        contaCorrente.alterarNome(input(f"Qual o novo nome a ser utilizado? "))

    if escolha == 2:
        contaCorrente.depositar(
            float(input(f"{contaCorrente.numeroConta} depositou quanto $$$? R$"))
        )

    if escolha == 3:
        contaCorrente.saque(
            float(input(f"{contaCorrente.numeroConta} tirou quanto $$$? R$"))
        )

    if escolha == 4:
        print(
            f"\n|-------------- Dados da conta --------------| \n\nNúmero da conta: {contaCorrente.numeroConta}\nNome: {contaCorrente.nome}\nSaldo: R${contaCorrente.saldo}"
        )

    escolha = int(
        input(
            f"O que será feito com a conta {contaCorrente.numeroConta}? \n\n1- Alterar o nome.\n2- Depositar.\n3- Sacar. \n4- Dados da conta \n0- Encerrar programa.\n\nOpção escolhida: "
        )
    )
