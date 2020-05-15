print([x ** 2 for x in range(5)])

print([n ** 2 for n in range(11) if n % 2 == 0])


pessoas = [' Ana ', 'manuela', 'FELIPe', 'PedrO']

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas]
print(pessoas_normalizadas)