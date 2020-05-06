# Mutable and Immutable datatypes

# Mutable

def f(m):
    m.append(3)
    print(m)


x = [1, 2]
f(x)
print(x == [1, 2])  # output is false.


# Immutable

x = (1, 2)
if x == (1, 2):
    print(True)

