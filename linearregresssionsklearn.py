import pandas
from sklearn import linear_model
df = pandas.read_csv("data/marks.csv")

X = df[['Phy', 'Chemistry']]
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