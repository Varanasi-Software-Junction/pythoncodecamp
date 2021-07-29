import cv2 as pp
import numpy as np

def solve(newpic):
    pass


def makeBGImage(pic):
    mx, my, mz = pic.shape
    newpic = makeTwoArray(mx,my)
    pic=invertImage(pic)
    pic=toBW(pic)
    for x in range(mx):
        for y in range(my):
            b = int(pic[x][y][0])  # Blue Value
        if b==255:
            newpic[x][y]=1
        else:
            newpic[x][y]=0
    return newpic


def makeTwoArray(length,width):
    return np.zeros(shape=(length,width))
def makeOneArray(arr):
    return arr.flatten()

def makeArrayFromList(list):
    return np.array(list)
def readImage(path):
    try:
        pic = pp.imread("K:\\Blogspot\\pics\\program output\\latest.png")
        return pic
    except:
        print("Error")
        return None
def invertImage(pic):
    mx, my, mz = pic.shape
    size=mx*my*mz
    avg=int(np.sum(pic)/size)
    for x in range(mx):
        for y in range(my):
            b = int(pic[x][y][0])  # Blue Value

            g = int(pic[x][y][1])  # Green Value

            r = int(pic[x][y][2])  # Red Value
            pic[x][y][0] = 255-b
            pic[x][y][1] = 255-g
            pic[x][y][2] = 255-r
    return pic


def toBW(pic):
    mx, my, mz = pic.shape
    size=mx*my*mz
    avg=int(np.sum(pic)/size)
    for x in range(mx):
        for y in range(my):
            b = int(pic[x][y][0])  # Blue Value

            g = int(pic[x][y][1])  # Green Value

            r = int(pic[x][y][2])  # Red Value
            currentavg=(r + g + b)/3
            if(currentavg>=avg):
                newvalue=255
            else:
                newvalue=0
            pic[x][y][0] = newvalue
            pic[x][y][1] = newvalue
            pic[x][y][2] = newvalue
    return pic

def toGrayScale(pic):
    pic=pic.copy()
    mx, my, mz = pic.shape

    for x in range(mx):

        for y in range(my):
            b = int(pic[x][y][0])  # Blue Value

            g = int(pic[x][y][1])  # Green Value

            r = int(pic[x][y][2])  # Red Value

            bwvalue = int((r + g + b) // 3)  # Average RGB

            pic[x][y][0] = bwvalue

            pic[x][y][1] = bwvalue

            pic[x][y][2] = bwvalue

            # print(r, g, b)

    return pic


