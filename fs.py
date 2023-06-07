import cv2
f_cascade = cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\Facedetection\\swetha.jpg")
img = cv2.imread('swetha.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = f_cascade.detectMultiScale(gray,1,1,4)
for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

cv2.imshow('r',img)
cv2.waitkey(0)