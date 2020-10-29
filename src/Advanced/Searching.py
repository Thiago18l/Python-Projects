print(['d', 'a', 'b', 'a'].index('a'))

from typing import Any


def linear_search(lst: list, value: Any) -> int:
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def linear_search_using_while(lst: list, value: Any) -> int:
    i = 0
    while i != len(lst) and lst[i] != value:
        i = i + 1
    if i == len(lst):
        return -1
    else:
        return i


lista = [4, 5, 3, 2, 1, 10]
print(linear_search(lista, 10))  # output is 5
print(linear_search_using_while(lista, 3))  # output is 2



