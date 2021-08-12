import pandas
from sklearn.linear_model import LinearRegression
df = pandas.read_csv("../data/marks.csv")

X= df[['Phy', 'Chemistry']]
y = df['Percent']
print(y)
print(X)
regvalue = LinearRegression()
regvalue.fit(X, y)



#predictedtotal = regvalue.predict([[10,20]])
print("Coeff=",regvalue.coef_)
print("Intercept",regvalue.intercept_)
#print(predictedtotal)
print(regvalue.score(X,y))