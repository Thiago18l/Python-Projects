
a = lambda x, y: x * y
print(a(2, 2))


lista = [
    ['P1', 13],
    ['P2', 17],
    ['P3', 20],
    ['P4', 44],
    ['P5', 55],
]
lista.sort(key=lambda item: item[1])
print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
