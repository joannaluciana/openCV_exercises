
import cv2
import numpy as np
img = cv2.imread("Resources/portret_small.jpg")
print(img.shape)
imgResize = cv2.resize(img,(600,500))

imgCroped = img[0:200,200:500]

cv2.imshow("image",img)
cv2.imshow("image resize",imgResize)
cv2.imshow("image croped",imgCroped)
cv2.waitKey(0)