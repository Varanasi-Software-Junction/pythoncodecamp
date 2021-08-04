import matplotlib.pyplot as plt
import numpy as np
def f1(x):
   return -3*x+5

x=np.linspace(-4,4,200)
"""y=[]
for i in range(len(x)):
    y.append(f1(x[i]))"""
#print(y)
plt.plot(x,f1(x),color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
#plt.xlim(0,7)# for zooming in x cordinate
#plt.ylim(0,7) #for zooming in y cordinate
plt.title("Lines")
plt.show()

