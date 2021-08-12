import numpy as np
import matplotlib.pyplot as plt
#from sklearn.metrics import r2_score
import pandas as pd
data = pd.read_csv("E:\pythoncodecamp\data\Share.csv")
print(data)
pf = np.polyfit(data['day'],data['value'],1)#gives coefficients
print(pf)
print(type(pf))
model = np.poly1d(pf)#gives equation obtained after regression
print(model)
print(type(model))
predictx=[9,10,11,12,13,14,15,20]
plt.scatter(data['day'],data['value'],color='red',marker=',',label="Given Data")#showing given dat on graph
plt.plot(predictx,model(predictx),color='green',marker='o',label="Prediction")
plt.xlabel('Day')
plt.ylabel('Share Value')
plt.legend()
plt.show()