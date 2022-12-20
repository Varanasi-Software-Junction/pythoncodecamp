a = [5, 6, 4, 9, 8, 2, 3, -7]
buckets = [3, 6, 9]
partitions = [0]
left = 0
print("original array ", a)
for i in buckets:
    right = len(a) - 1
    pivot = i
    while True:
        while left < right and a[left] < pivot:
            left += 1
        if left >= right:
            break
        while left < right and a[right] >= pivot:
            right -= 1
        if left >= right:
            break
        a[left], a[right] = a[right], a[left]
    partitions.append(left)

partitions.append(len(a))
print("partitions ", partitions)
print("partitioned array ", a)
for i in range(1, len(partitions)):
    start = partitions[i - 1]
    end = partitions[i]

    print(i, ":", a[start:end])

# print("Elements less than ",buckets[0], " are ",a[partitions[0]:partitions[1] +1])
# print("Elements less than ",buckets[1], " are ",a[partitions[0]:partitions[2] +1])
# print("Partitions", partitions)
