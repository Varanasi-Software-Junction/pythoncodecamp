

import cv2
import numpy as np
def readimage(readpath):
     a = cv2.imread(readpath) # reading image
     return a

def showimage(pic): # it will show the image
    cv2.imshow("Picture", pic)
    cv2.waitKey(0)

def imagepad(img,verticalp,horizontalp):
    pic=img.copy()
    mr, mc, mz = pic.shape  # mr=no.of row, mc=no.of column,mz =3 r g b values
    print(mr, mc, mz)
    for r in range(horizontalp):  # padding image 10% from above and below
        for c in range(mc):
            pic[r][c][0] = 255  # b value
            pic[r][c][1] = 255  # g value
            pic[r][c][2] = 255  # r value

            pic[mr - r - 1][c][0] = 255  # b value
            pic[mr - r - 1][c][1] = 255  # g value
            pic[mr - r - 1][c][2] = 255  # r value

    for r in range(mr):  # padding image from
        for c in range(verticalp):
            # pic[r][c] = [0, 0, 0]
            # pic[r][mc-c-1] = [255, 255, 255]
            # or
            pic[r][c][0] = 255  # b value
            pic[r][c][1] = 255  # g value
            pic[r][c][2] = 255  # r value

            pic[r][mc - c - 1][0] = 255  # b value
            pic[r][mc - c - 1][1] = 255  # g value
            pic[r][mc - c - 1][2] = 255  # r value

def verticalReverse(img):
    pic = img.copy()
    mr, mc, mz = pic.shape

    for r in range(mr):
        pic[r] = img[mr - 1 - r]
    return pic

def grayscale(pic):
    img=pic.copy()
    mr, mc, mz = img.shape
    for r in range(mr):
        for c in range(mc):
            red = int(img[r][c][2])
            green = int(img[r][c][1])
            blue = int(img[r][c][0])
            avg = int((red+green+blue)//3)
            img[r][c]=[avg,avg,avg]
    return img




def getThreshold(img):
    mr,mc,mz = img.shape
    sum = 0
    for r in range(mr):
        for c in range(mc):
            red   = int(img[r][c][2])
            green = int(img[r][c][1])
            blue  = int(img[r][c][0])
            avg   = int((red+green+blue)//3)
            sum += avg
    return int(sum//(mr*mc))

def blackwhite(img):
    pic = img.copy()
    t =35 #getThreshold(pic)
    mr,mc,mz = pic.shape
    for r in range(mr):
        for c in range(mc):
            blue=int(pic[r][c][0])
            green=int(pic[r][c][1])
            red=int(pic[r][c][2])
            avg = int((red+green+blue)//3)
            if avg<=t:
                pic[r][c]=[0,0,0]
            else:
                pic[r][c]=[255,255,255]
    return pic



readpath = "butterfly.jpg"
pic = readimage(readpath)
#pic1 = grayscale(pic)
pic2 = verticalReverse(pic)
#showimage(pic)
#print(pic)
#print(type(pic))
#showimage(pic)
#imagepad(pic1,20,20)
#showimage(pic1)
#revpic = verticalReverse(pic)
#showimage(revpic)
showimage(pic2)
#showimage(pic1)




