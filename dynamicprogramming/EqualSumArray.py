a = [1, 2, 5, 3, 0]
# print(a)
right = sum(a)
left = a[0]
# print(left,right)
n = len(a)
# print(n)
# print(0, left, right)
if left == right:
    print("Solution at ", 0, ", sum is ", left)
else:
    found = False
    for i in range(1, n):
        left += a[i]
        right -= a[i - 1]
        # print(i, left, right)
        if left == right:
            print("Solution at ", i, ", sum is ", left)
            found = True
            break
    if not found:
        print("Not found")
