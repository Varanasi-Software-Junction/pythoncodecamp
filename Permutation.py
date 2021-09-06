def Permute(l,li,n,pos):
    if pos > n-1:
        print(li)
        return

    for i in range(n):
        if i in li[:pos]:
            continue
        li[pos] = i
        #l[pos] = i
        #l.append(i)
        Permute(l,li,n,pos+1)
n=3
l=list(range(n))
l=['a','b','c']
n=len(l)
li=[]
for i in range(n):
    li.append(0)

Permute(l,li,n,0)

