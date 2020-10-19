
import cv2
import numpy as np
from stack import stackImages
from getCont import getContours



path = 'Resources/geom.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny,imgContour)

imgBlank=np.zeros_like(img)


imgStack = stackImages(0.6,([img,imgGray,imgBlur],
[img,imgContour,imgContour]))

cv2.imshow("Stacked ",imgStack)

cv2.waitKey(0)