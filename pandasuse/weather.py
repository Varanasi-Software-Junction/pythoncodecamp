import pandas as pd
import matplotlib.pyplot as plt
cum=[]
data = pd.read_csv("vns.csv")
print(data)
x=data["Celsius"]
x=data["Month"]
y=data["Celsius"]
prev=0
for item in y:
    cum =cum + [item + prev]
    prev=cum[len(cum)-1]
print(x)
print(y)
plt.grid()
plt.title("Varanasi Temperature")
plt.ylabel("Celsius")
plt.xlabel("Month")
plt.scatter(x,y,color="red",alpha=0.5)
plt.plot(x,y)
plt.plot(x,cum)
plt.show()