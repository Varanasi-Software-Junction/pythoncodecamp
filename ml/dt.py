import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("shows.csv")

d = {'A': 3, 'B': 2, 'C': 1}
df['Grade'] = df['Grade'].map(d)
print(d)
d = {'Pass': 1, 'Fail': 0}
df['Result'] = df['Result'].map(d)

features = ['Physics', 'Chemistry', 'Maths', 'Grade']
X = df[features]
y = df['Result']
print(X)
print(y)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[41, 70, 70, 3]]))

print("1 means 'Pass'")
print("0 means 'Fail'")
