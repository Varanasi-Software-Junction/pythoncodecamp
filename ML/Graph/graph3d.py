"""
This python program shows how to make 3d graph
"""
import matplotlib.pyplot as plt # importing matplotlib.pyplot
import numpy as np # importing numpy
def f(x,y): # Multi valued function
    return x**2+y**2
x= np.linspace(start=-7, stop=7, num=300) # it will create 300 numbers between 0 to 7
y= np.linspace(start=-7,stop=7, num=300) # it will create 300 numbers between 0 to 7
x,y=np.meshgrid(x,y) # it will create a meshgrid
fig = plt.figure() # making figure
ax = fig.gca(projection="3d") # for 3d graph
ax.set_xlabel('X',fontsize=12) # Naming x axis as 'X' and  fontsize = 12
ax.set_ylabel("Y",fontsize=20) # Naming y axis as 'Y' and  fontsize =20
ax.set_zlabel('Z',fontsize=12) # Naming z axis as 'Z' and  setting fontsize =
ax.plot_surface(x,y,f(x,y),cmap='winter', alpha=1) #plotting graph
plt.show() # showing graphs
