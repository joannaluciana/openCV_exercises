
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

hor = np.hstack((img,img))
ver = np.vstack((img,img))

cv2.imshow("horizontal",hor)
cv2.imshow("hvertical",ver)
cv2.waitKey(0)