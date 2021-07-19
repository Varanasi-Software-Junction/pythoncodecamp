import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data/abhi.csv') #retriving data from CSV file
print(data)
phy = data['Phy'] #storing only one column in phy
print(phy)
print(type(phy))
l=['Phy','Chem','Maths']
marks = data[l] # storing columns in marks
print(marks)
print(type(marks))
data['Percent'] = "new data" # adding new column in data
print(data)
data['Percent'] = (data['Phy']+data['Chem']+data['Maths'])/300*100 # data entering in the columns
print(data)

data.to_csv("data/new.csv", index =False)
print(data)
del data['Percent']
print(data)
query = data[(data['Phy']<=90) & (data['Phy']>=70)] #& fro and AND | for or
print(query)
query1 = data[((data['Phy']+data['Chem']+data['Maths'])/300*100>=60)]
print(query1)

data2= pd.read_csv("data/new.csv")
print(data2)
plt.plot(data2["Name"],data2["Percent"],color='green',marker='o')
plt.xlabel('Name')
plt.ylabel('Percent')
plt.title('Result')
plt.show()