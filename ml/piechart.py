import matplotlib.pyplot as plt
labels=["One","Two"]
data=[100,200]

#plt.figure(figsize=(20,20),dpi=10)
plt.pie(data,explode=[0.0,0.2],  labels=labels,textprops={'fontsize':46},startangle=45,autopct="%1.2f%%",colors=["red","green"])
plt.show()