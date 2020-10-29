from typing import Any

array = [4, 5, 3, 45, 1, 10, 4, 5, 3, 2, 1, 10, 4, 5, 3, 2, 1, 10, 4, 5, 3, 2, 1, 10, 4, 5, 3, 2, 1, 10]


def binary_search(lst: list, v: Any) -> int:
    i = 0
    j = len(lst) - 1
    while i != j + 1:
        m = (i + j) // 2
        if lst[m] < v:
            i = m + 1
        else:
            j = m - 1
    if 0 <= i < len(lst) and lst[i] == v:
        return i
    else:
        return -1


print(binary_search(array, 4))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
