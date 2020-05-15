class JogadorLoteria():
    def __init__(self, nome):
        self.nome = nome
        self.numeros = (13, 4, 52, 10, 25)

    def total(self):
        return sum(self.numeros)


jogador_1 = JogadorLoteria("Thiago")
jogador_2 = JogadorLoteria("Rafaela")

print(jogador_1.nome, jogador_1.numeros)
print(jogador_2.nome, jogador_2.numeros)
print(jogador_1 == jogador_2)
print(jogador_1.total())
