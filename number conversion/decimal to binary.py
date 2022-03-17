n = int(input("N=\n"))
b = [0 for i in range(n)]
n = len(b)
print(b)
i = n - 1
while True:
    i = n - 1
    while i >= 0:
        if b[i] == 1:
            b[i] = 0
            i -= 1
            continue
        if b[i] == 0:
            b[i] = 1
            print(b)
            break
    if not 0 in b:
        break
