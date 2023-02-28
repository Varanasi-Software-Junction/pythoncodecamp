a = [1, 2, 1, 4, 3, 66, -4, -8]
a.sort()
print(a)
valuetosearch = int(input("Enter value to search\n"))
n = len(a)
result = "Not Found"
left = 0
right = n - 1
while True:
    mid = (left + right) // 2
    print(left, mid, right)
    midvalue = a[mid]
    if midvalue == valuetosearch:
        result = "Found at " + str(mid)
        break
    if valuetosearch < midvalue:
        right = mid - 1
    else:
        left = mid + 1
    if left > right:
        break

print(result)
