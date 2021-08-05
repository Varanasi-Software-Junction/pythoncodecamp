import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,4]
x=numpy.array(x)
print(x.shape)
x=x.reshape(2,-1)
print(x.shape)
print(x)
x=x.reshape(-1)
print(x.shape)
print(x)
y = [2,4,6,8]
#x*2=[2,4,6,8]
#x*x=[1,4,9,16]
#sum(x) = 10


pf=numpy.polyfit(x,y,3)
print(pf)
print(type(pf))
model = numpy.poly1d(pf)
drv=model.deriv()
print(model([1,2,3,4]))
print(type(drv))
print(model)
print(drv)
coeff=r2_score(y, model(x))
print(coeff)
