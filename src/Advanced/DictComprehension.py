

myList = [
    ('1', 'value one'),
    ('2', 'value two'),
]
d1 = {x: y for x, y in myList}
print(d1)


# other way to do
d2 = dict(myList)
print(d2)
