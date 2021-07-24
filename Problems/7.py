



for i in range(100):
    n=i
    flag = 0
    if n == 1 or n == 0:
        flag = 1
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            flag = 1
    if flag == 0:
        print(n,)

