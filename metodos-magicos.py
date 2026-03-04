# 1)Qual palavra-chave (keyword) você usaria para ter acesso às propriedades e métodos de uma classe estando dentro dela?
# a) A palavra-chave new

# 2)

class Usuario():

    def __init__(self, primeiro, ultimo = None):
        self.primeiroNome = primeiro
        self.ultimoNome = ultimo

    def hello(self):
        return f"Olá {self.primeiroNome}"
    
    def getNomeCompleto(self):
        return f"Olá {self.primeiroNome} {self.ultimoNome}"

usuario1 = Usuario("Jonnie", "Bravo")

print(usuario1.hello())
print(usuario1.getNomeCompleto())