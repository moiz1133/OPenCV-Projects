#joining images
import cv2
import numpy as np
faceCascade=cv2.CascadeClassifier("resources/harcascade_frontal_face_default.xml")
img=cv2.imread("resources/man.jpg")
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gimg,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Image of man",img)
cv2.waitKey(0)