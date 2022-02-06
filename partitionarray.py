a = [1, 7, 5, 9, 7, 2, 5, 4, 3]
pivot = 5
start = 0
end = len(a) - 1
while True:
    while start < end and a[start] <= pivot:
        start += 1
    if start >= end:
        break
    while start < end and a[end] > pivot:
        end -= 1
    if start >= end:
            break
    a[start], a[end] = a[end], a[start]
print(a)
print(a[:end])
print(a[start:])