import cv2
import numpy as np

def getContours(img,imgCon):

    imgContour = img.copy()

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgCon, cnt, -1, (255,153,255),10)