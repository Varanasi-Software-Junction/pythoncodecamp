import matplotlib.pyplot as plt
import numpy as np
def sin(x):
    #res=x-(x**3/(3*2))+(x**5/(2*3*4*5))-(x**7/(2*3*4*5*6*7))
    s=1
    i=1
    sum=x
    term=x

    while not(term <= 0.0001 and term >= -0.0001) :
        k = x ** 2 / (2 * i * (2 * i + 1))

        term = (-1)**(i) *k*x
        print(term)
        sum += term
        i += 1
    return sum




print(sin(3.14))

x = np.linspace(start=-6.28,stop=6.28,num=100)

"""
plt.plot(x,sin(x),color='green')
plt.xlabel("X")
plt.ylabel("sinX")
plt.grid()
plt.show()"""