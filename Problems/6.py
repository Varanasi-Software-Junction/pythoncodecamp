def isPrime(n):

    if n == 1 :
        return False
    if n == 2 :
        return True
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False


    return False

l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(l)
sumprime=0
for i in range(3):
    for j in range(3):
        if i-j == 0 or i+j == 3-1:
            if isPrime(l[i][j]):
                sumprime += l[i][j]






