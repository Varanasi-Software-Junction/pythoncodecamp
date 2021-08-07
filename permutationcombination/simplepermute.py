n=3
s="ABC"
l=list(range(n))
for i in range(n):
    l[0]=i
    for j in range(n):
        if j in l[:1]:
            continue
        l[1]=j
        for k in range(n):
            if k in l[:2]:
                continue
            l[2]=k
            print(s[l[0]],s[l[1]],s[l[2]])