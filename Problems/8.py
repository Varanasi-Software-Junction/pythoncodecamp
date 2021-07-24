def permute(s,n,l,j):
    for i in range(n):
        if i not in l:
            l.append(i)
        permute(s,n,l,j-1)


s='kashi'
l=[]
n=len(s)