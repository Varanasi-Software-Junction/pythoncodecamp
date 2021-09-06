import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("result.csv")
print(data)
d={"fail":0,"pass":1}
data["result"]=data["result"].map(d)
#print(data)
l=["Maths","Physics","Chemistry"]
x=data[l]
y=data['result']
print(x)
print(y)
#dtree= DecisionTreeClassifier()
dtree = DecisionTreeClassifier().fit(x,y)
print(dtree.predict([[50,45,50]]))