from itertools import groupby

students = [
    {'nome': 'Thiago', 'nota': 'A'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Ray', 'nota': 'D'},
    {'nome': 'Martin', 'nota': 'A'},
    {'nome': 'Morty', 'nota': 'B+'},
    {'nome': 'Henry', 'nota': 'A'},
]

sort = lambda item: item['nota']
students.sort(key=sort)
for student in students:
    print(student)

students_grouped = groupby(students, sort)
for group, values in students_grouped:
    print(f'Agrupamento: {group}')
    count = len(list(values))
    print(f'{count} students who scored {group}')
