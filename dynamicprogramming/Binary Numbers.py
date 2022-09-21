n = 2
bin = [0 for i in range(n)]
print(bin)

while True:
    over = True
    for i in range(n - 1, -1, -1):
        if bin[i] == 0:
            bin[i] = 1
            over = False
            break
        else:
            bin[i] = 0
    if over:
        break
    print(bin)
