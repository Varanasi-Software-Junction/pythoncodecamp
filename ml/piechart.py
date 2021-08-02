import matplotlib.pyplot as plt
labels=["One","Two","Three",'4','5','6']
data=[10,20,60,1,2,3]
plt.pie(data,labels=labels,autopct="%1.2f%%")
plt.scatter(data,data,alpha=0.5,color="#FF0000")
plt.title("PIE Graph")
plt.legend()
plt.show()
