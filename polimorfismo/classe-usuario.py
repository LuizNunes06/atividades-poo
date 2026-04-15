class Usuario:
    pontos = 0
    numeroDeArtigos = 0
    
    # Métodos vão aqui

    def setNumeroDeArtigos(self, nart):
        self.numeroDeArtigos = nart


    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos
    
    def calcPontuacao():
        pass

class Autor(Usuario):

    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 10 + 20
        return self.pontos
    
class Editor(Usuario):

    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 6 + 15
        return self.pontos
    
autor1 = Autor()
autor1.setNumeroDeArtigos(8)

print(f"Pontuação do autor1: {autor1.calcPontuacao()}")

editor1 = Editor()
editor1.setNumeroDeArtigos(15)

print(f"Pontuação do editor1: {editor1.calcPontuacao()}")