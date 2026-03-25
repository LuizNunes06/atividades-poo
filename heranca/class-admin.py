class Usuario():
    def __init__(self, nome = ""):
        self.__nomeUsuario = nome

    def setNomeUsuario(self, novoNome):
        self.__nomeUsuario = novoNome

    def getNomeUsuario(self):
        return self.__nomeUsuario

class Admin(Usuario):

    def __init__(self, nome=""):
        super().__init__(nome)

    def escrevaNome(self):
        print("Admin")
    
    def digaOla(self):
        print(f"Olá Admin, {self.getNomeUsuario()}")


admin1 = Admin("Baltazar")

admin1.digaOla()


# 8 - A causa do problema é que classe tem o atibuto nome como privado e não pode ser acessado pela classe filha

# 9 - O código foi alterado para usar protected