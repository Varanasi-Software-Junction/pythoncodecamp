+import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x * x + x + 1
def df(x):
    return 2 * x + 1
ex1=np.linspace(start=-3,stop=3,num=100)
print(type(ex1))
print(ex1)
plt.grid()
plt.plot(ex1,f(ex1))
plt.plot(ex1,df(ex1))
plt.show()
previousx=-2
upperlimit=2
lowerlimit=-2
gradient=df(previousx)
for i in range(30):
    mid = (lowerlimit + upperlimit )/2
    gradient = df(mid)
    if gradient<0:
        lowerlimit=mid
    else:
        upperlimit=mid
mid = (lowerlimit + upperlimit )/2
print(mid)



