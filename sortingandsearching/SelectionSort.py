a = [4, 3, 7, -5, 8]  # The input list
print("Input list", a)
n = len(a)  # Get length of list
for i in range(n - 1):  # Loop through the array one time less than the length of the list
    min, minpos = a[i], i  # Set the min to a[i] the current element and position of the min to i
    for j in range(i + 1, n):  # Loop through the array and find the min and minpos
        if a[j] < min:
            min = a[j]
            minpos = j
    a[i], a[minpos] = a[minpos], a[i]  # Swap a[i] and a[minpos]
    print("Array after ", i + 1, " iterations ", a)
print("Sorted Array ", a)
