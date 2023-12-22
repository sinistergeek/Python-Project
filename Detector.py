import os
import sys
import cv2

def detector():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(os.path.dirname(sys.argv[0]) + '/haarcascade_frontalface_alt2.xml')
    while True:
        ret,frame=cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
            send_mail(frame=frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1)& 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
detector()

