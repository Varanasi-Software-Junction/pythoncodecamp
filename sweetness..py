choc =['x','a','b','c','d','e','f']
sweet =[0,2,3,7,3,2,2]
bitter =[0,5,4,1,4,9,3]

for i in range (1,len(choc)-1):
    s=sweet[i]
    b=bitter[i]
    c=choc[i]
    minpos=i
    for j in range(i,len(choc)):
        if (sweet[j]<s) or (sweet[j]==s and bitter[j]>b) or(sweet[j]==s and bitter[j]==s and choc[j]>c):
            s=sweet[j]
            b=bitter[j]
            c=choc[j]
            minpos=jm

    sweet[i],sweet[minpos]=sweet[minpos],sweet[i]
    bitter[i],bitter[minpos]=bitter[minpos],bitter[i]
    choc[i],choc[minpos]=choc[minpos],choc[i]

print(choc[1:])







