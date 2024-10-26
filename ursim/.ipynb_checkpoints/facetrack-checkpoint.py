import cv2
import time
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
t1=time.time()
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Face Tracker',frame)
    if cv2.waitKey(1) & 0xff==27 or time.time()-t1>=100:
        break
cap.release()
cv2.destroyAllWindows()