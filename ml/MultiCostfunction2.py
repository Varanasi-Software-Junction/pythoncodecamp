import matplotlib.pyplot as plt
from sympy import symbols, diff
from matplotlib import cm
import numpy as np

def f(x,y):
    r = 3**(-x*x - y*y)
    return 1/(r+1)
def doFit():
    a, b = symbols('x, y')
    multiplier = 0.1
    max_iter = 900
    params = np.array([-3, 5.0])
    print("DiffX = ", diff(f(a, b), a))
    print("DiffY =",  diff(f(a,b), b))
    for n in range(max_iter):
        gradient_x = diff(f(a, b), a).evalf(subs={a: params[0], b: params[1]})
        gradient_y = diff(f(a, b), b).evalf(subs={a: params[0], b: params[1]})
        gradients = np.array([gradient_x, gradient_y])
        params = params - multiplier * gradients
    print("Gradients = ", gradients)
    print("Params = ", params)
    print("Function at Min = ", f(params[0],params[1]))
    return params[0],params[1]
error=0.00001
x = np.linspace(start = -4, stop=4, num=200)
y = np.linspace(start = -4, stop =4 , num = 200)
x,y = np.meshgrid(x,y)
s,t=doFit()

fig = plt.figure(figsize=(16,12))
ax = fig.gca(projection='3d')
ax.set_xlabel("X",fontsize=20)
ax.set_ylabel("Y",fontsize=20)
ax.scatter(s,t,f(s,t),marker='o')

ax.plot_surface(x,y,f(x,y),cmap='binary',alpha = 0.5)
plt.show()
