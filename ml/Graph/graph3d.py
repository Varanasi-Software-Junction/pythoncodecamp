import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
def f(x,y):
    return x**2+y**2
x= np.linspace(start=0, stop=0, num=300)
y= np.linspace(start=0,stop=0, num=300)
x,y=np.meshgrid(x,y)
x1=np.linspace(start=-2, stop=2, num=300)
y1= np.linspace(start=-2,stop=2, num=300)
x1,y1=np.meshgrid(x1,y1)
print(x1)

fig = plt.figure(figsize=(20,20))
ax = fig.gca(projection="3d")
ax.set_xlabel('X',fontsize=12)
ax.set_ylabel("Y",fontsize=20)
ax.scatter(0,0,0,marker=',')
ax.plot_surface(x1,y1,f(x1,y1),cmap=cm.winter,alpha=0.4)
#ax.plot_surface(x,y,f(x,y),cmap='binary', alpha=1)
plt.show()
