l=['A','B','C']
n=3
for i in range(1,n + 1):
    for j in range(1,n + 1):
        if i==j:
            continue
        for k in range(1,n + 1):
            if j==k or i==k:
                continue
            print(i,j,k)
            print(l[i-1], l[j-1], l[k-1])



