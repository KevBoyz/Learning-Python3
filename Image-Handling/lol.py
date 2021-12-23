import cv2
import cvzone

ah = cv2.imread('assets/ah1.png', cv2.IMREAD_UNCHANGED)
p = cv2.imread('assets/person.jpg')

r = cvzone.overlayPNG(p, ah, [10, 10])
cv2.imshow('lol', r)
cv2.waitKey()