a = [1, 2, 5, 3, 0]
sumtofind = 3
currentsum = 0
n = len(a)
prev = 0
next = 0
while True:
    if next >= n:
        break
    currentsum += a[next]
    if currentsum == sumtofind:
        print("Found ", prev, next,a[prev:next+1])
    while currentsum > sumtofind:
        currentsum -= a[prev]
        prev += 1
        if prev > next:
            break
    next += 1
