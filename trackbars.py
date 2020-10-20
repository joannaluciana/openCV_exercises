import cv2
import numpy as np


frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
h_min = cv2.createTrackbar("Hue min", "Trackbars", 0, 179, empty)
h_max = cv2.createTrackbar("Hue max", "Trackbars", 179, 179, empty)
s_min = cv2.createTrackbar("Sat min", "Trackbars", 0, 255, empty)
s_max = cv2.createTrackbar("Sat max", "Trackbars", 255, 255, empty)
v_min = cv2.createTrackbar("Val min", "Trackbars", 0, 255, empty)
v_max = cv2.createTrackbar("Val max", "Trackbars", 255, 255, empty)


while True:

    _, img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val max", "Trackbars")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow("Horizontal Stackin", hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
