#warp perspective
import cv2
import numpy as np
width,height=114,160
img=cv2.imread("resources/card.jpg")
pts1=np.float32([[433,61],[545,33],[470,223],[584,195]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("cutted pic",imgOutput)
cv2.imshow("Full pic",img)
cv2.waitKey(0)