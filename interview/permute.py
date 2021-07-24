l=['A','B','C']
n=len(l)
for i in range(n):
    p1=[l[i]]
    for j in range(n):
        p2=p1.copy()
        if l[j] in p2:
            continue
        p2=p2 + [l[j]]
        for k in range(n):
            p3=p2.copy()
            if l[k] in p3:
                continue
            p3=p3 + [l[k]]
            print(p3)