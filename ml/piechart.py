import matplotlib.pyplot as plt
labels=["One","Two","Three"]
data=[10,20,60]
#plt.figure(figsize=(20,20),dpi=10)
plt.pie(data,labels=labels,autopct="%1.2f%%")
plt.show()