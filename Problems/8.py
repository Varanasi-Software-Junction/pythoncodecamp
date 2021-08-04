count = 0
def permute(s,l,n,pos):

    if pos >= n:
        global count
        count = count +1
        #print(l)
        print(count,end=".")
        for j in range(n):


            print(s[l[j]] , end='')
        print()
        return
    for i in range(n):
        if i in l[:pos]:
            continue
        else:
            l[pos]=i
            permute(s,l,n,pos+1)


s='kashi'
n=len(s)
l=[]
for i in range (n):
    l.append(0)
n=len(s)
permute(s,l,n,0)