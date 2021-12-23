import cv2
import cvzone as cz

vid = cv2.VideoCapture(0)
algorithm = cv2.CascadeClassifier('trained-files/haarcascades/haarcascade_frontalface_default.xml')
ah = cv2.imread('assets/ah1.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = vid.read()
    # cv2.imwrite('assets/st.png', frame)
    faces = algorithm.detectMultiScale(frame)
    for x, y, l, a in faces:
       try:
            img = cz.overlayPNG(frame, ah, [x-50, y-60])
            cv2.imshow('Display', img)
       except:
           pass
       # frame[y_offset:y_end, x_offset:x_end] = ah
    if cv2.waitKey(1) == 'q':
        break
