# 1) Nós usamos o modificador de acesso private a fim de:

# d) B e C estão corretas


print("|=========== Usuario ===========|\n")


class Usuario:

    def __init__(self, primeiro, ultimo=None):
        self.__primeiroNome = primeiro
        self.ultimoNome = ultimo

    def getPrimeiroNome(self):
        return f"Primeiro nome: {self.__primeiroNome}"

    def getNomeCompleto(self):
        return f"Olá {self.__primeiroNome} {self.ultimoNome}"

    def setPrimeiroNome(self, novoPrimeiroNome):
        self.__primeiroNome = novoPrimeiroNome

        print("Novo nome: ", self.__primeiroNome)


usuario1 = Usuario("Jonnie", "Bravo")

print(usuario1.getPrimeiroNome())

usuario1.setPrimeiroNome("Novo")

print(usuario1.getPrimeiroNome())

print("\n\n|========== Empregado ==========|\n")


class Empregado:

    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.__salario = salario
        self.projeto = projeto

    def trabalho(self):
        return f"Nome: {self.nome} \nProjeto: {self.projeto}\n"

    def mostrar(self):
        return f"Nome: {self.nome} \nSalário: {self.__salario}\n"

    def setSalario(self, novoSalario):
        self.__salario = novoSalario


empregado = Empregado("Jonnie", 2000, "Analista")

print(empregado.trabalho())
print(empregado.mostrar())
empregado.setSalario(2200)
print(empregado.mostrar())

print("\n\n|========== Robo ==========|\n")


class Robo:

    def __init__(self, nome, ano):
        self.__nome = nome
        self.__anoConstrucao = ano

    def diga_alo(self):
        return f"Olá \nMeu nome é: {self.__nome}\nFui construido no ano de {self.__anoConstrucao}\n"

    def set_infos(self, novoNome=None, novoAno=None):

        if novoNome:
            self.__nome = novoNome

        if novoAno:
            self.__anoConstrucao = novoAno

        print(f"Após alterações: \nNome: {self.__nome} \nAno: {self.__anoConstrucao}\n")


robo1 = Robo("R2D2", 1977)

print(robo1.diga_alo())

robo1.set_infos("Wall-e")
robo1.set_infos("", 2008)

robo1.set_infos("Sahelanthropus", 1980)
robo1.diga_alo()

print("\n\n|========== Laptop ==========|\n")

class Laptop:
    def __init__(self, preco):
        self.__preco = preco

    def get_preco(self):
        return f"Preço do laptop: {self.__preco}"
    
    def set_preco(self, novoPreco):
        self.__preco = novoPreco

laptop1 = Laptop(3200)

print(laptop1.get_preco())

laptop1.set_preco(3999)

print(laptop1.get_preco())

print("|=========== Pessoa ===========|\n")


class Pessoa:

    def __init__(self, primeiro, ultimo=None):
        self.__primeiroNome = primeiro
        self.__ultimoNome = ultimo

    def getPrimeiroNome(self):
        return f"Primeiro nome: {self.__primeiroNome}"

    def getUltimoNome(self):
        return f"Ultimo nome: {self.__ultimoNome}"

    def setPrimeiroNome(self, novoPrimeiroNome):
        self.__primeiroNome = novoPrimeiroNome

        print("Novo nome: ", self.__primeiroNome)

    
    def setUltimoNome(self, novoUltimoNome):
        self.__ultimoNome = novoUltimoNome

        print("Novo nome: ", self.__ultimoNome)


pessoa1 = Pessoa("João", "Carvalho")

print(pessoa1.getPrimeiroNome())
print(pessoa1.getUltimoNome())

print("\n")

pessoa1.setPrimeiroNome("Bruno")
pessoa1.setUltimoNome("Silva")

print("\n")

print(pessoa1.getPrimeiroNome())
print(pessoa1.getUltimoNome())
