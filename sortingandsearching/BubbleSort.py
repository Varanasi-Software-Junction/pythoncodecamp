a = [4, 3, 7, -5, 8]  # The input list
print("Input list", a)
n = len(a)  # Get length of list
for i in range(n - 1):  # Loop through the array one time less than the length of the list
    for j in range(0, n-1):  # Loop through the array and find reverse ordered pairs and swap them
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]  # Swap a[j] and a[j+1]
    print("Array after ", i + 1, " iterations ", a)
print("Sorted Array ", a)
