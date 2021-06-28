#joining images
import cv2
import numpy as np

def getContours(imag):
    #finding the contours form the image
    contours,heirarchy=cv2.findContours(imag,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        #getting area
        area=cv2.contourArea(cnt)
        print(area)
        #drawing the shapes on img2
        cv2.drawContours(img2,cnt,-1,(255,0,0),1)
        #to find the parameter of shpaes
        peri=cv2.arcLength(cnt,True)
        #to find the corners of shape
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))
        x, y, w, h = cv2.boundingRect(approx)
        #checking the shapes
        if len(approx)==3: objectType="Triangle"
        elif len(approx)==4:
            apectRatio=w/float(h)
            if apectRatio>0.95 and apectRatio<1.05:
                objectType="Square"
            else:objectType="Rectangle"
        elif len(approx)>4:objectType = "Circle"
        else: objectType="None"
        #making a bounding box around our shapes

        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img2,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)


img=cv2.imread("resources/shapes.png")
img2=img.copy()
greyImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bImage=cv2.GaussianBlur(greyImage,(7,7),1)
cImage=cv2.Canny(bImage,20,200)
getContours(cImage)
cv2.imshow("Real image",img)
cv2.imshow("drawed image",img2)
cv2.waitKey(0)