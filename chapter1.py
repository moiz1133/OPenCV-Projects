import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),6)
cv2.rectangle(img,(0,0),(250,350),(0,0,255))

cv2.putText(img," hello moiz asif ",(300,250),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
cv2.imshow("image",img)
cv2.waitKey(0)
