

def quickSort(a, left, right):
    level += 1
    noofcalls += 1
    if level > maxdepthofrecursion:
        maxdepthofrecursion = level
    if left >= right:
        level -= 1
        return
    pivot = a[left]
    finalposition = left
    for i in range(left + 1, right + 1):
        if a[i] >= pivot:
            continue
        finalposition += 1
        a[i], a[finalposition] = a[finalposition], a[i]
    a[left], a[finalposition] = a[finalposition], a[left]
    quickSort(a, left, finalposition - 1)
    quickSort(a, finalposition + 1, right)
    level -= 1
noofcalls = 0
maxdepthofrecursion = 0
level = 0
print(level)


a = [5, 6, 4, 9, 8, 2, 3, 7]
print("Input array", a)
quickSort(a, 0, len(a) - 1)
print("Sorted array", a)
print("No of calls", noofcalls, ", Maxdepth", maxdepthofrecursion)
