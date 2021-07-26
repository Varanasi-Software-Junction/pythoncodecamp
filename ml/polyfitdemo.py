import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
data=pd.read_csv("../pandasuse/vns.csv")
x = [1,2,3,4]

predictx=list(range(1,101))

y=data["Celsius"]
n=len(y)
x=list(range(1,n + 1))
#predictx=x
print(n)
print(y)
pf=numpy.polyfit(x,y,1)
print(pf)
print(type(pf))
model = numpy.poly1d(pf)
drv=model.deriv()
print(type(drv))
print(model)
print(drv)
plt.title("Varanasi Temperature")
plt.scatter(x, y,color="red",linewidth=10,label="Temp data")
plt.plot(x, y,color="pink",linewidth=10,label="Temp data",alpha=0.6)
plt.plot(predictx, model(predictx),color="blue",linewidth=1,label="Predicted Data")
plt.scatter(predictx, model(predictx),color="blue",linewidth=1,label="Predicted Data")
plt.plot(predictx, drv(predictx),color="green",linewidth=4,label="Derivative")
plt.legend()
plt.show()