"""
This Python program how to mark different points on graph
"""
import matplotlib.pyplot as plt # importing matplotlib.pyplot
"""
If we have to mark the points (0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)
then we'll create a list of x containing all the values serially and 
we'll do the same thing for y
"""
x = [0,1,2,3,4,5,6]
y = [0,1,2,3,4,5,6]
plt.bar(x,y,color='yellow') #plotting Bar graph
plt.plot(x,y,color='red',marker='') #plotting line graph
plt.scatter(x,y,color='green',marker='o') # plotting point graph
plt.xlabel('X') # naming x axis as X
plt.ylabel('Y') # naming y axis as Y
plt.title('Line ') # naming thee graph
plt.show() # it will show the graph