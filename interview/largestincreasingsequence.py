l=[2,5,9,1,4,5,3,4,6,8,0,1]
n=len(l)
l= l + [l[n-1]-1]
print(l)
n=n+1
maxlength = -1
maxsequence = []
currentseq = [l[0]]

for i in range(1,n):
    prev=l[i-1]
    current=l[i]
    if current>=prev:
        currentseq = currentseq + [current]
    else:
        if (len(currentseq)) > maxlength:
            maxlength = len(currentseq)
            maxsequence = currentseq.copy()
        currentseq = [current]
print(maxsequence)

