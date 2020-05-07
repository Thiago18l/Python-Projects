a_string = 'Hello World'
print(a_string)
print(a_string[0])
print(a_string[0:5])  # the first five characters


# Sets

basket = {'Apple', 'Orange', 'Apple', 'pear', 'orange', 'banana'}
print(basket)  # Duplicates will be removed

a = set('abracadabra')
print(a)
a.add('z')
print(a)

# Frozen sets

b = frozenset('asdadasa')
print(b)

cities = frozenset(['Frankfurt', "Basel", "Freiburg"])
print(cities)
