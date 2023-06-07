
import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\Facedetection\\sri-IT.jpg")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\Facedetection\\sri-IT.jpg")

img = cv2.imread("C:\\Users\\user\\Desktop\\Facedetection\\sri-IT.jpg",1)

while True:
    _, img = cv2.read()
    gray = cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiscale(gray,1,1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    cv2.waitkey(0)
