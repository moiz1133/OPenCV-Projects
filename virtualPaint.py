# webcam code
import cv2
import numpy as np

vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,150)

myColors=[[0,76,100,44,255,255],
          [51,51,0,93,255,255],
          [137,83,0,167,255,255]]
colorValues=[[51,51,255],
             [0,204,0],
             [255,102,178]]
points=[] ##points[x,y,colorId]
def findColor(img,myColors,colorValues):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newpoints=[]
    for color in myColors:
        low = np.array(color[0:3])
        high = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, low, high)
        # image printing
        # cv2.imshow(str(color[0]), mask)
        x,y=getContours(mask)
        cv2.circle(img2,(x,y),10,colorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newpoints.append([x,y,count])
        count+=1
    return newpoints


def getContours(imag):
    #finding the contours form the image
    contours,heirarchy=cv2.findContours(imag,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        #getting area
        area=cv2.contourArea(cnt)
        #drawing the shapes on img2
        cv2.drawContours(img2,cnt,-1,(255,0,0),1)
        #to find the parameter of shpaes
        peri=cv2.arcLength(cnt,True)
        #to find the corners of shape
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y
def drawOnCanvas(points,colorValues):
    for point in points:
        cv2.circle(img2, (point[0], point[1]), 10, colorValues[point[2]], cv2.FILLED)


while True:
    success, img = vid.read()
    img2=img.copy()
    newpoints=findColor(img,myColors,colorValues)
    if len(newpoints)!=0:
        for newP in newpoints:
            points.append(newP)
    if len(points)!=0:
        drawOnCanvas(points,colorValues)
    cv2.imshow("My video", img2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
