import cv2
from pymodbus.client import ModbusTcpClient
import time
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
client=ModbusTcpClient('192.168.0.133',port=502)
connection=client.connect()
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
t1=time.time()
if connection:
    print('Connected')
    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        for (x,y,w,h) in faces:
            client.write_coil(16,True)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            Cx=int(x+w/2)
            Cz=int(y+h/2)
            client.write_register(128,Cx)
            client.write_register(129,Cz)
        cv2.imshow('Face Tracker',frame)
        if cv2.waitKey(1) & 0xff==27 or time.time()-t1>=60:
            client.write_coil(16,False)
            client.close()
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('No connection')