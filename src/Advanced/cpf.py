

cpf = '11245257401'
new_cpf = cpf[:-2]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)


sequencia = new_cpf == str(new_cpf[0]) * len(cpf)

if cpf == new_cpf and not sequencia:
    print("Válido")
else:
    print("Inválido")
