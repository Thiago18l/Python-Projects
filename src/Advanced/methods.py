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