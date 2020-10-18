
import cv2
img = cv2.imread("Resources/portret_small.jpg")

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

cv2.imshow("gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.waitKey(0)