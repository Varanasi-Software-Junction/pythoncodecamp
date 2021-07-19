import matplotlib.pyplot as plt
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
newx=3
prevx=0
m=0.1

for i in range(300):
   prevx=newx
   gradient=df(prevx)
   newx=prevx-m*gradient


print(newx)
print(df(newx))


