



def mergesort(a, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    mergesort(a, left, mid)
    mergesort(a, mid + 1, right)
    temp = [0 for x in range(right - left + 1)]
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1
    if i <= mid:
        for p in range(i, mid + 1):
            temp[k] = a[p]
            k += 1
    else:
        for p in range(j, right + 1):
            temp[k] = a[p]
            k += 1
    for t in range(left, right + 1):
        a[t] = temp[t - left]


a = [22, 3, 4, -6, 5, 4]
print(a)
mergesort(a, 0, len(a) - 1)
print(a)






