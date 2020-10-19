import cv2
import numpy as np

def getContours(img,imgCon):

    imgContour = img.copy()

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
           cv2.drawContours(imgCon, cnt, -1, (255,153,255),5)
           peri = cv2.arcLength(cnt,True)
           approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
           print(peri, len(approx))
           x,y,w,h = cv2.boundingRect(approx)
           if len(approx) ==3: objectType ="tri"
           else:objectType="None"
        #    cv2.rectangle(imgCon,(x,y),(x+w,y+h),(255,153,255),5)
           cv2.rectangle(imgCon,(x,y),(x+w,y+h),(255,153,255),3)
           cv2.putText(imgCon,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,153,255),3)

