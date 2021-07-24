c=['a','b','c']
l=[0,0,0]
n=len(l)

for i in range(2**n):
    print(l)
    for j in range(n):
        if l[j] == 1:
            print(c[j],end="")
    print()
    for j in range(n-1,-1,-1):
        if l[j] ==0:
            l[j] = 1
            break
        l[j] = 0
count =0
for i in range(3):

    for j in range(3):
        if i == j:
            continue
        for k in range(3):
            if i==k or j==k:
                continue

            print(c[i],c[j],c[k])
            count +=1

print(count)