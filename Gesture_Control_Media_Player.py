import numpy as np
import cv2
import math
import pyautogui

capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret,frame = capture.read()
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    crop_image = frame[100:300,100:300]
    blur = cv2.GaussianBlur(crop_image,(3,3),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(hsv,np.array([2,0,0]),np.array([20,255,255]))
    kernel = np.ones(5,5)
    dilation = cv2.dilate(mask=2,kernel,iterations=1)
    erosion = cv2.erode(dilation,kernel,iterations=1)
    filtered = cv2.GaussianBlur(erosion,(3,3),0)
    ret,thresh = cv2.threshold(filtered,127,255,0)
    cv2.imshow("Thresholded",thresh)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
