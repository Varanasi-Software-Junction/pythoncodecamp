import scratch
def permutation(pos,n,l):
    if pos>=n:
        return
    for i in range(n):
        if i in l[:pos]:
            continue
        l[pos]=i
        permutation(pos+1,n,l)
        if pos==n-1:
            scratch.count += 1
            print(scratch.count,l)


x=4
permutation(0,x,list(range(x)))