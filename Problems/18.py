"""def isprime(n):
    if n==1:
        return 0
    if n==2:
        return 1
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 0
    return 1
l=[]
n=6
i=1
while len(l)<6:
    if isprime(i):
        l.append(i)
    i += 1
print(l)
n = 2
"""
n=8
l = [2]
i=3
while len(l)<n:
    flag = 1
    for j in l:
        if j>int(i**(1/2))+1:
            continue
        if i%j == 0:
            flag=0
    if flag == 1:
        l.append(i)
    i += 1
print(l)


