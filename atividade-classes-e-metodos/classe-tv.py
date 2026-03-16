class Tv:
    canais = [2, 4, 5, 7, 9, 11, 13, 16, 18, 21, 23, 25, 27, 30]

    def __init__(self, volume, canal=canais[0]):
        self.canal = canal
        self.volume = volume

    def escolheCanal(self, novoCanal):
        if novoCanal in self.canais:
            self.canal = novoCanal

        else:
            print("!!! Canal inexistente, tente consultar a lista de canais !!!")

    def aumentarVolume(self, aumento):
        if aumento > 100 - self.volume:
            self.volume == 100

        else:
            self.volume += aumento

        print(f"O volume foi alterado para {self.volume}")

    def diminuirVolume(self, reducao):
        if reducao > self.volume:
            self.volume == 100

        else:
            self.volume -= reducao

        print(f"O volume foi alterado para {self.volume}")

    def listarCanais(self):
        print("\n|-------- Lista de canais --------|\n")

        for canal in self.canais:
            print(f"{canal:^35}")


tv = Tv(30)

escolha = int(
    input(
        f"O que deseja fazer? \n\n1- Mudar canal.\n2- Aumentar volume.\n3- Diminuir volume.\n4- Ver lista de canais.\n\nOpção escolhida: "
    )
)

while escolha != 0:

    if escolha == 1:
        tv.escolheCanal(int(input("Qual será o canal? ")))

    if escolha == 2:
        tv.aumentarVolume(int(input(f"O volume será aumentado em quanto? ")))

    if escolha == 3:
        tv.diminuirVolume(float(input(f"O volume será diminuido em quanto? ")))

    if escolha == 4:
        tv.listarCanais()

    escolha = int(
        input(
            f"O que deseja fazer? \n\n1- Mudar canal.\n2- Aumentar volume.\n3- Diminuir volume.\n4- Ver lista de canais.\n\nOpção escolhida: "
        )
    )
