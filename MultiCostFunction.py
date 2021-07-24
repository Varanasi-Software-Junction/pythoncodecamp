import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def f(x,y):

    r = (x**3+y**3)()
    return r
def df(x):
    return 4 * x**3 -8*x
error = 0.00001
x=np.linspace(start=-2, stop=2,num=200)
y=np.linspace(start=-2, stop=2,num=200)
x,y= np.meshgrid(x,y)
fig = plt.figure(figsize=(200,200))
ax = fig.gca(projection='3d')
ax.set_xlabel("X",fontsize=20)
ax.set_ylabel("Y",fontsize=20)
ax.set_zlabel("Z",fontsize=20)
ax.plot_surface(x,y,f(x,y),cmap=cm.winter,alpha=1)
plt.show()