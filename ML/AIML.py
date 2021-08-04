def linearRegression(px,py):
    sumx = 0
    sumy = 0
    sumxy = 0
    sumxx = 0


    n = len (px)
    for i in range(n):
        x = px[i]
        y = py[i]
        sumx += x
        sumy += y
        sumxx += x*x
        sumxy += x*y

    a=(sumxy-sumx*sumy/n)/(sumxx-(sumx**2)/n)
    b=(sumy-a*sumx)/n
    print(sumx,sumy,sumxy,sumxx)
    return a,b
x=[0,1,2,3,4]
y=[4,6,8,10,12]
#print(x.__len__())
a,b=linearRegression(x,y)
print(a,b)
#y=ax+b


