class ContaBancaria:
    def __init__(self, titular, saldo, juros = 0):
        self.titular = titular
        self.saldo = saldo
        self.juros = juros

    def getSaldo(self):
        return self.saldo
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"\nDepósito de R${valor} realizado com sucesso\n saldo atual: R${self.saldo}")

    def retirada(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"\nRetirada de R${valor} realizada com sucesso\n saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente")

    
    def calcularJuros(self):
        juros_calculados = self.saldo * self.juros
        self.saldo += juros_calculados
        print(f"\nJuros de R${juros_calculados} calculados e adicionados ao saldo\n saldo atual: R${self.saldo}")

class ContaPoupanca(ContaBancaria):

    def __init__(self, titular, saldo, juros=0.08):
        super().__init__(titular, saldo, juros)


class ContaCorrente(ContaBancaria):
    
    def __init__(self, titular, saldo, juros=0.02):
        super().__init__(titular, saldo, juros)


contaCorrente = ContaCorrente("João", 1000)
contaPoupanca = ContaPoupanca("Maria", 2000)

listaContas = [contaCorrente, contaPoupanca]

escolhaConta = int(input("Escolha a conta para realizar operações:\n1 - Conta Corrente\n2 - Conta Poupança \n\nOpção escolhida: "))

escolhaOperacao = int(input("Escolha a operação:\n1 - Depósito\n2 - Retirada\n3 - Calcular Juros \n4 - Mudar Conta \n\nOpção escolhida: "))

while escolhaOperacao > 0:
    if escolhaConta == 1:
        conta = contaCorrente
    elif escolhaConta == 2:
        conta = contaPoupanca
    else:
        print("Opção de conta inválida")
        break

    if escolhaOperacao == 1:
        valor = float(input("Digite o valor para depósito: "))
        conta.deposito(valor)
    elif escolhaOperacao == 2:
        valor = float(input("Digite o valor para retirada: "))
        conta.retirada(valor)
    elif escolhaOperacao == 3:
        conta.calcularJuros()

    elif escolhaOperacao == 4:
        escolhaConta = int(input("\nEscolha a conta para realizar operações:\n1 - Conta Corrente\n2 - Conta Poupança \n\nOpção escolhida: "))
    else:
        print("Opção de operação inválida")

    escolhaOperacao = int(input("\nEscolha a operação:\n1 - Depósito\n2 - Retirada\n3 - Calcular Juros \n4 - Mudar Conta \n\nOpção escolhida: "))