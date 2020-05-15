class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
      return {'nome': self.nome, 'salario': self.salario}


fabio = Funcionario("Fabio", 800)
print(fabio.dados())


class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()


fernando = Admin("Fernando", 1300)
print(fernando.dados())
print(fernando.atualizar_dados('Thiago'))
print(fernando.nome)