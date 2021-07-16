import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
df = pandas.read_csv("data/marks.csv")
percent=list(df['Percent'])
phy=list(df["Phy"])

X = df[['index','Phy' ]]
y = df['Percent']
print(y)
print(X)
regvalue = linear_model.LinearRegression()
regvalue.fit(X, y)




predictedtotal = regvalue.predict([[10,20]])
print("Coeff=",regvalue.coef_)
print("Intercept",regvalue.intercept_)
print(predictedtotal)
print(regvalue.score(X,y))
plt.plot(phy,percent)
plt.show()