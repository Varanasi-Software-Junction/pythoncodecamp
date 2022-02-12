# for n in range(5,0,-1):
#    print(n,n-1,n &(n-1),bin(n & (n-1)), bin(n),bin(n-1))
n = 9
print(n, bin(n))
while n:
    n = n & (n - 1)
    print(n, bin(n))
