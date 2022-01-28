def isValid(limit, d, a, n):
    sum = 0
    i = 0
    divisions = 0
    while i <= n - 1:
        if a[i] > limit:
            return False
        sum = sum + a[i]
        if sum > limit:
            sum = sum - a[i]
            #print(sum, "<=", limit, " at ", i)
            sum = a[i]
            divisions += 1
            if divisions > d:
                return False
            if divisions == d and i <= n - 1:
                return False
        i += 1
    return True


a = [10, 1, 7, 4, 6, 9, 4, 5, 9, 19, 3, 4, 2, 4, 9]
n = len(a)
# print(n)
d = 3

upperlimit = sum(a)
lowerlimit = upperlimit // 3
result = 0
mid = (lowerlimit + upperlimit) // 2
while True:
    if isValid(mid, d, a, n):
        result = mid
        upperlimit = mid - 1
    else:
        lowerlimit = mid + 1
    mid = (lowerlimit + upperlimit) // 2
    #print(lowerlimit,mid,upperlimit)
    if lowerlimit > upperlimit:
        break

#result = isValid(48, 3, a, n)
print(result)
