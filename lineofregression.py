import  matplotlib.pyplot as plt
def linearregression(px,py):
    sigmay=0
    sigmax=0
    sigmaxy=0
    sigmax2=0
    n=len(px)
    for i in range(n):
        x=px[i]
        y=py[i]
        sigmax += x
        sigmay += y
        sigmaxy += x*y
        sigmax2 += x*x

    print(sigmax,sigmay,sigmax2,sigmaxy)
    b=(sigmax * sigmay - n * sigmaxy)/(sigmax * sigmax - n * sigmax2)
    a=(sigmay - b * sigmax)/n
    return a,b


x=[12,15,21,25]
y=[50,70,100,120]
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
result = linearregression(x,y)
print(result)