
import cv2
import numpy as np
def empty(a):
    pass

path = 'Resources/cards.jpg'
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
h_min = cv2.createTrackbar("Hue min","Trackbars", 0, 144,empty)
h_max = cv2.createTrackbar("Hue max","Trackbars", 144, 144,empty)
s_min = cv2.createTrackbar("Sat min","Trackbars", 0, 255,empty)
s_max = cv2.createTrackbar("Sat max","Trackbars", 255, 255,empty)
v_min = cv2.createTrackbar("Val min","Trackbars", 0, 166,empty)
v_max = cv2.createTrackbar("Val max","Trackbars", 166, 166,empty)


while True:
    img=cv2.imread(path)
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat max","Trackbars")
    v_min = cv2.getTrackbarPos("Val min","Trackbars")
    v_max = cv2.getTrackbarPos("Val max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask=mask)
#  two img in one
    cv2.imshow("Original",img)
    cv2.imshow("ColorHSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)