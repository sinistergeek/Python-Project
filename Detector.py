import os
import sys
import cv2

def detector():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(os.path.dirname(sys.argv[0]) + '/haarcascade_frontalface_alt2.xml')
    while True:
        ret,frame=cap.read()

