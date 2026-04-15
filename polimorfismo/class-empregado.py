class Empregado:

    def __init__(self, nome):
        self.nome = nome

    def pagar_salario(self):
        pass

class EmpregadoHora(Empregado):

    def __init__(self, nome, valor_hora, horas_trabalhadas = 20):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def pagar_salario(self):
        return self.valor_hora * self.horas_trabalhadas
    
class EmpregadoMes(Empregado):

        def __init__(self, nome, salario):
            super().__init__(nome)
            self.salario = salario

        def pagar_salario(self):
             return self.salario

empregadoHora = EmpregadoHora("Bob", 120)    
empregadoMes = EmpregadoMes("Silva", 1700)

for empregado in (empregadoHora ,empregadoMes):
     print(f"{empregado.nome} recebeu R$ {empregado.pagar_salario()} este mês")