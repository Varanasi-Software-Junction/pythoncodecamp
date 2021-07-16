import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[7,8,11,1.3,16,15,-1,-.2,0,3.3]
#plt.figure(figsize=(0,1000))
#plt.xlim(0,100)
#plt.ylim(-10,100)
#fig=plt.figure()

plt.scatter(x,y,color='green',marker='o')
plt.plot(x,y,color='yellow',linewidth=10,alpha=0.5)
plt.xlabel("Time ")
plt.ylabel("Income")
#plt.bar(x,y,color='green')
plt.title("Time Vs Income")
plt.show()