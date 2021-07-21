l = [1,3,6,88,90]
maxdif=-1
maxdifp =-1

for i in range(len(l)-1):
    dif = l[i+1]-l[i]
    if dif <0:
        dif = -dif
    if dif>maxdif:
        maxdif = dif
        maxdifp =i

print(l[maxdifp], l[maxdifp+1])