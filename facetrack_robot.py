import cv2
import time
import URsocket.UR as UR
import numpy as np
start_joint=[0,-69.87,-128.01,14.64,93.23,-49.38]
ur=UR.control('172.20.10.9')
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
t1=time.time()
def Deg2Rad(deglist):
    radlist=[np.deg2rad(x) for x in deglist]
    return radlist

if ur:
    ur.moveJ(Deg2Rad(start_joint),0.5,0.1,0,0)
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            Cy=int(x+w/2)
            Cz=int(y+h/2)
            errorY=int(frame.shape[1]/2 - Cy)
            errorZ=int(frame.shape[0]/2 - Cz)
            ur.speedL([0,errorY/1000,errorZ/1000,0,0,0],0.5,5,0.5,False)
        cv2.imshow('Face Tracker',frame)
        if cv2.waitKey(1) & 0xff==27 or time.time()-t1>=60:
            break
    cap.release()
    cv2.destroyAllWindows()
    ur.disconnect()
else:
    print('No connection')
