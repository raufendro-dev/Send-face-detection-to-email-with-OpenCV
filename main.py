#Send-face-detection-with-OpenCV
#By raufendro
import cv2
import numpy as np
import time
from mail import proses
import os



timestr = time.strftime("%Y%m%d-%H%M")


wajah = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

obj=cv2.VideoCapture(0)
obj.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
obj.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(timestr+'.avi', fourcc, 30.0, (640,480))

if not obj.isOpened():
    print('Kamera mati')
    exit()

q=False
while (q==False):
    ret, Frame = obj.read()
    
    if ret==True:
        abu=cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
        i=0
        daftar_wajah=wajah.detectMultiScale(abu, scaleFactor=1.3, minNeighbors=2)
        
        for (x, y, w, h) in daftar_wajah:
            i=i+1
            aku = cv2.rectangle(Frame, (x, y), (x+w, y+h), (60, 255, 0), 2)
            cv2.putText(aku, 'Manusia'+str(i), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)
            #print(i)
            if i >= 1:
                print("Ada manusia")
                cv2.imwrite('Manusia.jpg', Frame)
                #out.write(Frame)
                
            else:
                break

        #cv2.imshow('Kamera', Frame)
        if os.path.isfile('Manusia.jpg'):
         proses()
         os.remove("Manusia.jpg")    
            
        else:
            print("Tidak ada Manusia")
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            q=True
            break
       

obj.release()
cv2.destroyAllWindows()