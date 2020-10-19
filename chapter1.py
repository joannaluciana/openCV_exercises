
import cv2
import numpy as np
from stack import stackImages

path = 'Resources/geom.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgStack = stackImages(0.6,([img,imgGray,imgBlur]))

cv2.imshow("Stacked ",imgStack)

cv2.waitKey(0)