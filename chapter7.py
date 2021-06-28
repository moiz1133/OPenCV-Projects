#joining images
import cv2
import numpy as np
def empty(a):
    pass
#Making a track bar
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,280)
#defining values for each trackbar
cv2.createTrackbar("Hue min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue max","Trackbars",24,179,empty)
cv2.createTrackbar("sat min","Trackbars",198,255,empty)
cv2.createTrackbar("sat max","Trackbars",255,255,empty)
cv2.createTrackbar("val min","Trackbars",46,255,empty)
cv2.createTrackbar("val max","Trackbars",255,255,empty)

while True:
    img = cv2.imread("resources/car.jpg")
    # converting image to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # getting values form trackbars
    hmin = cv2.getTrackbarPos("Hue min", "Trackbars")
    hmax = cv2.getTrackbarPos("Hue max", "Trackbars")
    smin = cv2.getTrackbarPos("sat min", "Trackbars")
    smax = cv2.getTrackbarPos("sat max", "Trackbars")
    vmin = cv2.getTrackbarPos("val min", "Trackbars")
    vmax = cv2.getTrackbarPos("val max", "Trackbars")
    print(hmin,hmax,smin,smax,vmin,vmax)
    #making masked image
    low=np.array([hmin,smin,vmin])
    high = np.array([hmax, smax, vmax])
    mask=cv2.inRange(imgHSV,low,high)
    #image printing
    cv2.imshow("Image chnaged",mask)
    resultedImage=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Without color", img)
    cv2.imshow("With color", imgHSV)
    cv2.imshow("Resulted image",resultedImage)
    cv2.waitKey(1)

