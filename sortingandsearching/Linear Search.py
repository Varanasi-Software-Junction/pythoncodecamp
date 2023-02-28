a = [1, 2, 1, 4, 3, 66, -4, -8]
valuetosearch = int(input("Enter value to search\n"))
n = len(a)
result = "Not Found"
for i in range(n):
    if valuetosearch == a[i]:
        result = "Found at " + str(i)
        break
print(result)
