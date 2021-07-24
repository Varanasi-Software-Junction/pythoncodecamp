l=[2,5,9,1,4,5,3,4,6,8,0,1,2,3,4,5,6]
l.append(l[len(l)-1]-1)
maxpos=0
maxcount=0
count=0
presentpos=0

for i in range(len(l)-1):
    if l[i+1] > l[i]:
        count += 1
    else:
        count += 1
        if count > maxcount:
            maxcount = count
            maxpos = presentpos
        count = 0
        presentpos = i + 1
print(maxpos,maxcount)
for j in range(maxpos, maxpos+maxcount):
    print(l[j],end=',')



