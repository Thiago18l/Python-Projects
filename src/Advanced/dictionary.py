

d1 = {'chave': 'valor da key'}
d1['new_key'] = 'value of new key'

print(d1['chave'])

d2 = dict(chave1 ="valor1", chave2="valor2")
print(d2['chave1'])
d3 = {
    'str': 'valor',
    1: 'valor 1',
    (1, 3): 'Tuple',
}
print(d3['str'])

# Alter value of key str
d3['str'] = "New value for str"
print(d3['str'])

for v in d3.values():
    print(v)
