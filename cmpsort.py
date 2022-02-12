import functools as ft


def bitcount(second, first):
    print(first, second)
    while first * second:
        first = first & (first - 1)
        second = second & (second - 1)

    return second - first


def sortBySetBitCount(arr):
    arr.sort(key=ft.cmp_to_key(bitcount))
    return arr


l = [1, 2, 3, 4, 5]
l = sortBySetBitCount(l)
print(l)
