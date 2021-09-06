l=[1,1,1,2,2,2,2,3,3,4,4,4,3]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)