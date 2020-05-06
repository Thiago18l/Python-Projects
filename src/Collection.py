# Collection types in Python

int_list = [1, 2, 3]
string_list = ['Bob', 'Anne', 'Thiago']


# list can be empty

empty_list = []

# mixed data types in list

mixed_list = [1, True, 2.2, None]

# lists can contain another list as its element

nested_list = [['a', 'b', 'c'], [1, 2, 3]]

print(nested_list)


names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0])  # Alice
print(names[2])  # Craig

# Indices can also be negative which means counting from the end of the list (-1 being the index of the last element)

print(names[-1])  # Eric
print(names[-4])  # Bob


names[0] = 'Thiago'

print(names)

names.append("João")
print(names)

names.insert(0, "Urahara")
print(names)

names.remove("Thiago")
print(names)

print(names.index("Bob"))

# COUNT LENGTH OF LIST

print(len(names))

# COUNT OCCURRENCE OF ANY ITEM IN LIST

numbers_list = [1, 1, 2, 4, 4, 6, 8]
print(numbers_list.count(2))

# REVERSE THE LIST
numbers_list.reverse()
print(numbers_list)

# or

numbers_list[::-1]
print(numbers_list)

print(names.pop())

for element in names:
    print(element)

# Tuples

ip_andress = ('10.10.0.1', 8080)
print(ip_andress)

one_member_tuple = ('One member',)
one_member_tuple = 'Only member'

# Dictionaries

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

ca_capital = state_capitals['California']
print(ca_capital)

for capital in state_capitals:
    print('{} is the capital of {}'.format(state_capitals[capital], capital))

# Set

first_names = {'Thiago', 'Beth', 'Charlie'}

print(first_names)

my_list = [1, 2, 3]
print(my_list)
my_set = set(my_list)
print(my_set)

for name in first_names:
    print(name)
name = 'Thiago'
if name in first_names:
    print(name)
else:
    print("Dont found")


# Defaultdict

from collections import defaultdict
state_capitals = defaultdict(lambda: 'Boston')


