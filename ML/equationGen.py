#from sympy import symbols,diff
import cv2
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np
"""class PredictorImage:
    def __init__(self,pic,label):
        self.pic = pic
        self.label = label"""
def readimg(path):
    a= cv2.imread(path)
    return a
def showimg(img,imgname):
    cv2.imshow(imgname,img)
    cv2.waitKey(0)
def f(a): #
    sum=0
    for i in range(len(a)):
        if a[i] == 1:
            sum += (i+1)**2
    sum +=1
    return sum
def getThreshold(pic):
    mr,mc,mz=pic.shape
    sum = 0
    for r in range(mr):
        for c in range(mc):
            avg = (int(pic[r][c][0])+int(pic[r][c][1])+int(pic[r][c][2]))//3
            sum += avg
    return int(sum//(mr*mc))
def blackwhite(img):
    pic = img.copy()
    t= getThreshold(pic)
    mr,mc,mz=pic.shape
    for r in range(mr):
            for c in range(mc):
                avg = (int(pic[r][c][0]) + int(pic[r][c][1]) + int(pic[r][c][2])) // 3
                if avg <= t:
                    pic[r][c]=[0,0,0]
                else:
                    pic[r][c]=[255,255,255]
    return pic
def grayscale(img):
    pic = img.copy()
    mr,mc,mz=pic.shape
    for r in range(mr):
        for c in range(mc):
            avg = int(int(pic[r][c][0])+int(pic[r][c][1])+int(pic[r][c][2])//3)
            pic[r][c] = [avg,avg,avg]
    return pic
def onedarray(pic):
    mr,mc,mz=pic.shape
    l=[]
    #count =1;
    for r in range(mr):
        for c in range(mc):
            #print(count)
            if pic[r][c][1] == 255:
                l.append(0)
            else:
                l.append(1)
            #count +=1
    return l
def imgvalue(img):
    bw = blackwhite(img)
    oned = onedarray(bw)
    return f(oned)
def classification(n,imgvalue1,imgvalue2,imgvalue3,imgvalue4,imgvalue5):
    l=[]
    for i in range(len(n)):
        if n[i] <= imgvalue4:
             l.append(4)
        elif n[i] <= imgvalue2:
             l.append(2)
        elif n[i] <= imgvalue3:
             l.append(3)

        elif n[i] <= imgvalue5:
             l.append(5)
        elif n[i] <= imgvalue1:
             l.append(1)
    return l



#listofpics=[PredictorImage(readimg("one.png",1))]
pic1 = readimg("one.PNG")
showimg(pic1,"One")
pic2 = readimg("two.PNG")
pic3 = readimg("three.PNG")
pic4 = readimg("four.PNG")
pic5 = readimg("five.PNG")
showimg(pic5,"five")
print("1",imgvalue(pic1))
print("2",imgvalue(pic2))
print("3",imgvalue(pic3))
print("4",imgvalue(pic4))
print("5",imgvalue(pic5))
l = [1,2,3,4,5]
p = [imgvalue(pic1),imgvalue(pic2),imgvalue(pic3),imgvalue(pic4),imgvalue(pic5)]
imgv = np.linspace(4646160000,7994260792,200)
c=classification(imgv,p[0],p[1],p[2],p[3],p[4])
print(len(c))
print(len(imgv))
plt.plot(imgv,c,color="red",marker="o")

plt.show()

