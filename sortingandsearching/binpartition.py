def binPartition(a, value):
    right = len(a) - 1
    left = 0

    while True:
        mid = (left + right) // 2
        if value == a[mid]:
            return mid - 1
        if value < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
        if left > right:
            if a[mid] < value:
                return mid
            return mid - 1


a = [2, 4, 5, 6, 77, 88]
result = binPartition(a, 78)
print(a)
print(result)
if result >= 0:
    print(a[result])
