from cv2 import cv2
import os
import os.path
from datetime import datetime,date

def openCam():
    datsets = 'webcam'
    sub_data = 'data'
    path = os.path.join(datasets,sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    webcam=cv2.VideoCapture(0,cv2.CAp_DSHOW)
    (_,im) = webcam.read()
    now = str(datetime.now())
    now = now.replace(':','')
    now = now.replace('-','')
    now = now.replace('.','')
    now = now.replace(' ','')
    cv2.imwrite(f'webcam\\data\\{now}.png'im)
    img = f'webcam\\data\\{now}.png'
    convert(img)
