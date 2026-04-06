class Conta():

    def __init__(self, numero, saldo, cliente):
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente
    
    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")

    def getSaldo(self):
        print(f"Saldo: R${self._saldo}")

class CEspecial(Conta):

    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self._limite = limite

    def debitar(self, valor):
        if self._saldo + self._limite >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")