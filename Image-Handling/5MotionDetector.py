import cv2

vid = cv2.VideoCapture(0)
while vid.isOpened():
    ret, frame = vid.read()
    cv2.imshow('inter', frame)
