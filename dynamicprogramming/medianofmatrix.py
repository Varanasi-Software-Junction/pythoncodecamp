def partition(a, pos):
    left, right = 0, len(a) - 1
    while True:
        pivot = a[left]
        fp = left
        for i in range(left + 1, right + 1):
            if a[i] >= pivot:
                continue
            fp += 1
            a[i], a[fp] = a[fp], a[i]

        a[left] = a[fp]
        a[fp] = pivot
        if fp == pos:
            return pivot
        if pos < fp:
            right = fp - 1
        else:
            left = fp + 1


r = 3

c = 3
m = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
a = []
for i in m:
    a.extend(i)
print(a)
medianpos = (r * c - 1) // 2
print(medianpos)
print(partition(a, medianpos))
print(a)
