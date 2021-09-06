def NoofDays(n,p,k):
    countd=0
    for i in range(k):
        for j in range(i,n,k):
            #print(t,j)
            countd+=1
            #print(countd)
            if j == p:
                return countd
n,p,k=input().split()
n= int(n)
p=int(p)
k=int(k)
print(NoofDays(n,p,k))
