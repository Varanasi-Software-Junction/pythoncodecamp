import matplotlib.pyplot as plt
import numpy as np
def gradient_descent(derivative_function,initialguess,multiplier,error):
    listvalues=[]
    listgradient=[]
    for i in range(300):
        prevx = initialguess
        gradient = derivative_function(prevx)
        listvalues = listvalues + [initialguess]
        listgradient = listgradient + [gradient]
        initialguess = prevx - multiplier * gradient
        diff = abs(initialguess - prevx)
        if diff < error:


            return initialguess,listvalues,listgradient,diff




def f(x):
    return x**4 - 4*x**2 + 5
def df(x):
    return 4 * x**3 - 8*x
error=0.00001
ex1=np.linspace(start=-2,stop=2,num=1000)
print(type(ex1))
print(ex1)
plt.grid()

plt.plot(ex1,f(ex1))

plt.plot(ex1,df(ex1))
plt.legend(['Cost Function','Derivative'])

finalvalue,x,y,diff= gradient_descent(df,2,0.1,0.0001)
plt.plot(x,y)
plt.show()




