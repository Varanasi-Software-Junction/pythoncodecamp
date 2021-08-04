import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1-x
data=pd.read_csv("test.csv")
print(data)
roll=data["Rollno"]
t1 =data["t1"]
t2 = data["t2"]
print(roll,t1,t2)
plt.pie(t1,labels=roll,autopct="%1.2f%%")

plt.title("Marks in test1")
plt.show()
plt.pie(t2,labels=roll,autopct="%1.2f%%")
plt.title("Marks in test2")
plt.show()
data["t2-t1"]=data["t2"]-data["t1"]
print(data)
plt.title("Marks in test1")
benefit=0
notbenefit=0
for i in data['t2-t1']:
    if i>0:
        benefit +=1
    else:
        notbenefit +=1
print(benefit,notbenefit)
plt.pie([benefit,notbenefit],labels=["Benefitted","Not Benefitted"],autopct="%1.2f%%",explode=[0.1,0.1])
plt.title("Deciding")
plt.show()

range=["0-15","15-18","18-21","21-23","23-26"]
n = [0,0,0,0,0]
for i in data["t1"]:
    if i < 15:
        n[0] += 1
    elif i < 18:
        n[1] += 1
    elif i < 21:
        n[2] += 1
    elif i < 23:
        n[3] += 1
    elif i < 26:
        n[4] += 1

plt.pie(n,labels=range,autopct="%1.2f%%")
plt.show()
x = np.linspace(0,1,100)
plt.plot(x,f(x),color="red")
plt.xlim(0,1)
plt.ylim(0,1)
plt.title("happening Vs Not happening")
plt.show()
