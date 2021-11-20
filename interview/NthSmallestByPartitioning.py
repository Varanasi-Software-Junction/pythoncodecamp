a = [3, 5, 2, 11, 6, 4]
n = 3
left = 0
right = len(a) - 1
print(a)
while True:
    pivot = a[left]
    fp = left
    for i in range(left + 1, right + 1):
        if a[i] >= pivot:
            continue
        fp += 1
        a[fp], a[i] = a[i], a[fp]
    if fp == n:
        print("Element found ", pivot)
        break
