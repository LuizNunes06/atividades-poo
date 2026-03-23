class Usuario():
    def __init__(self, nome = ""):
        self.__nomeUsuario = nome

    def setNomeUsuario(self, novoNome):
        self.__nomeUsuario = novoNome

class Admin(Usuario):

    def __init__(self, nome=""):
        super().__init__(nome)

    def escrevaNome(self):
        print("Admin")
    
    def digaOla(self):
        print(f"Olá Admin, {self.__nomeUsuario}")


admin1 = Admin("Baltazar")

admin1.digaOla()