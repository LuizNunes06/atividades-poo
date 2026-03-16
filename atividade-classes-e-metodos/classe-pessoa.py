class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        print("\n|-------------- Mudança na idade --------------|\n")
        if self.idade <= 21:
            if (21 - self.idade) >= anos:
                self.altura = anos * 0.005

            else:
                self.altura = (21 - self.idade) * 0.005

            print(f"Agora a altura é: {self.altura} ")

        self.idade += anos
        print(f"Nova idade: {self.idade}")

    def engordar(self, massa):
        print("\n|-------------- Mudança no peso --------------|\n")
        self.peso += massa

        print(f"O novo peso é: {self.peso}")

    def emagrecer(self, massa):
        print("\n|-------------- Mudança no peso --------------|\n")
        self.peso -= massa

        print(f"O novo peso é: {self.peso}")

    def crescer(self, alturaCm):
        print("\n|-------------- Mudança na altura --------------|\n")

        self.altura += (alturaCm / 100)

        print(f"A nova altura é: {self.altura}m")


pessoa = Pessoa(
    input("Informe o nome da pessoa: "),
    int(input("Informe a idade da pessoa: ")),
    float(input("Informe o peso da pessoa(em kg): ")),
    float(input("Informe a altura da pessoa(em metros): ")),
)

escolha = int(
    input(
        f"O que acontecerá com {pessoa.nome}? \n\n1- Envelhecer.\n2- Engordar.\n3- Emagrecer.\n4- Crescer.\n\nOpção escolhida: "
    )
)

while escolha != 0:

    if escolha == 1:
        pessoa.envelhecer(int(input(f"Quantos anos {pessoa.nome} envelheceu? ")))
    
    if escolha == 2:
        pessoa.engordar(float(input(f"{pessoa.nome} engordou quantos kilos? ")))

    if escolha == 3:
        pessoa.emagrecer(float(input(f"{pessoa.nome} emagreceu quantos kilos? ")))

    if escolha == 4:
        pessoa.crescer(float(input(f"Quantos centimetros {pessoa.nome} cresceu? ")))

    escolha = int(input(
        f"O que acontecerá com {pessoa.nome}? \n\n1- Envelhecer.\n2- Engordar.\n3- Emagrecer.\n4- Crescer.\n0- Nada, encerrar programa.\n\nOpção escolhida: "
    ))

