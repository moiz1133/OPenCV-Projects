# webcam code
import cv2
import numpy as np

vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,150)
while True:
    success, img = vid.read()
    cv2.imshow("My video", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
