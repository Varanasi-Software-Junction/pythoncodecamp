import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,0,0,0,1,1,1,1,1,1,1]
#x*2=[2,4,6,8]
#x*x=[1,4,9,16]
#sum(x) = 10


pf=numpy.polyfit(x,y,4)
model = numpy.poly1d(pf)
drv=model.deriv()
print(model(3))
print(model(4))
coeff=r2_score(y, model(x))
print(coeff)
plt.plot(x,y)
plt.show()
