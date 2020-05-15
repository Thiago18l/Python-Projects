class Funcionario():
    aumento = 1.04
    def __init__(self, nome, salario: float):
        self.nome = nome
        self.salario: float = salario

    def dados(self):
      return {'nome': self.nome, 'salario': self.salario.__round__(2)}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    @classmethod
    def new_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento

    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return 'Não é um dia útil'
        return 'É um dia útil'


thiago = Funcionario("Thiago", 1200)
print(thiago.dados())
thiago.aplicar_aumento()
print(thiago.dados())
Funcionario.new_aumento(1.10)
thiago.aplicar_aumento()
print(thiago.dados())
joao = Funcionario("Joao", 5000)
joao.aplicar_aumento()
print(joao.dados())

import datetime

minha_data = datetime.date(2020, 5, 16)
print(thiago.dia_util(minha_data))