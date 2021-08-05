import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
data=pd.read_csv("prediction.csv")
print(data)
d={'pass':1,'fail':0}
data['result']=data['result'].map(d)
#print(data['result'])
features=['phy','math','chem']
x=data[features]
y=data['result']
#print(x)
#print(y)
dtree=DecisionTreeClassifier()
dtree=dtree.fit(x,y)
print(dtree.predict([[30,30,30]]))
print("1 means pass")
print("0 means fail")