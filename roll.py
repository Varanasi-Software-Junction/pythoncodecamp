import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("H:\youtubepython\info1.csv")
x=df['rollno']
y=df['name']
print(x)
print(y)
plt.scatter(x,y,color='red',marker='o')
plt.show()