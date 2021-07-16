import matplotlib.pyplot as plt
import pandas
#from sklearn import linear_model
df = pandas.read_csv("H:\youtubepython\info.csv")
#x=list(df['sno'])
#y=list(df["age"])

x = df[['sno' ]]
y = df['age']
print(x)
print(y)
plt.plot(x,y,color='red',marker='o')
plt.show()