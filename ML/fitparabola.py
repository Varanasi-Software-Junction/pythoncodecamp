def fitparabola(lx,ly):
    sigmax=0
    sigmay=0
    sigmaxy=0
    sigmax2=0
    sigmax3=0
    sigmax4=0
    sigmax2y=0
    n=len(lx)
    for i in range(n):
        x=lx[i]
        y=ly[i]
        sigmax += x
        sigmay += y
        sigmaxy += x*y
        sigmax2 += x*x
        sigmax3 += x*x*x
        sigmax4 += x*x*x*x
        sigmax2y +=0
    print(sigmax,sigmay,sigmaxy,sigmax2,sigmax3,sigmax4,sigmax2y)

    #a=(sigmay-b*sigmax+c*sigmax2)/n
    #return c
x=[0,1,2,3,4]
y=[1,1.8,1.3,2.5,6.3]
result=fitparabola(x,y)
print(result)


