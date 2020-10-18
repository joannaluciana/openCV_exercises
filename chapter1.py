
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
# img[200:500,200:500]=255,0,0
# matrix size
cv2.line(img,(0,0),(300,300),(0,255,0),4)
cv2.imshow("image", img)
cv2.waitKey(0)