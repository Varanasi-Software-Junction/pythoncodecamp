def mult(l1,l2):
    l=[]
    n=len(l1)
    for i in range(n):
        l=l + [l1[i] * l2[i]]
    return sum(l)
def booleanGenerate(n):
    l=[]
    for i in range(n):
        l= l + [0]
    output=[l]
    newl=l.copy()
    while(True):

        for i in range(n):
            if newl[i]==0:
                newl[i]=1
                break
            else:
                newl[i]=0
        output=output + [newl]
        if( sum(newl)==n):
            return output
        newl=newl.copy()

intensity = [1,-2,3,-3,4,-5]

n=len(intensity)
x=booleanGenerate(n)
for item in x:
    value=mult(item,intensity)
    if value<=0:
        print(item,value)

