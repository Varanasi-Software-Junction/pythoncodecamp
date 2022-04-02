"""
4,3,9,-9,7
min 4,3,-9,
"""


def QuickSort(a, left, right):
    if left >= right:
        return
    pivot = a[left]
    fp = left
    for i in range(left + 1, right + 1):
        if a[i] >= pivot:
            continue
        fp += 1
        a[fp], a[i] = a[i], a[fp]
    a[fp], a[left] = a[left], a[fp]
    QuickSort(a, left, fp - 1)
    QuickSort(a, fp + 1, right)


l = [3, 2, 1, 4, -5]
print(l)
QuickSort(l, 0, len(l) - 1)
print(l)
