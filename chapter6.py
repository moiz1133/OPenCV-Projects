#joining images
import cv2
import numpy as np
img=cv2.imread("resources/cat1.jpg")
#horizaontal stacked
imgstacked=np.hstack((img,img))
cv2.imshow("Double omg",imgstacked)
#vertical stacked
imgstacked=np.vstack((img,img))
cv2.imshow("Vertical img",imgstacked)

cv2.waitKey(0)