
import numpy as np
import cv2
#---loading haarcascade detector---
face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#---Loading the image-----

img = cv2.imread("C:\\Users\\user\\Desktop\\Facedetection\\sri-IT.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('default.xml', img)
cv2.waitKey(0)
cv2.destroyAllWindows()