import cv2 as pp
import imagelibrary as imglib
import matplotlib.pyplot as plt

x=list(range(0,101))
y=[]
for i in x:
    if i < 40:
        y = y + [0]
    elif i<50:
        y = y + [3]
    elif i<60:
        y= y + [2]
    else:
        y = y + [1]
plt.plot(x,y,linewidth=4,color='blue')
plt.scatter(x,y, color="red", alpha=0.7)
plt.show()

pic = imglib.readImage ("K:\\Blogspot\\pics\\program output\\latest.png")
newpic=imglib.makeBGImage(pic)
print(newpic)
output = pp.imshow("Show Picture", newpic)
pp.waitKey(0)
pic=imglib.invertImage(pic)
output = pp.imshow("Show Picture", pic)
pp.waitKey(0)
pic=imglib.toBW(pic)
pp.imshow("Show Picture", pic)
#pp.imwrite("K:\\Blogspot\\pics\\program output\\bw.png", pic)  # Save to disk
output = pp.waitKey(0)

