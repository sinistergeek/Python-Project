import cv2
import numpy as np
import imutils
frame = cv2.imread('test.jpeg')
frame = cv2.imread(frame,(600,600))
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(25,1))
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,25))
print('horizontal kernel: {}'.format(horizontal_kernel))
print('vertical kernel : {}'.format(vertical_kernel))
horizontal_lines = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,horizontal_kernel,iterations=2)
vertical_lines = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,vertical_kernel,iterations=2)
cnts = cv2.findContours(horizontal_lines,cv2.RETR_EXTERNAL,cv2.findContours(vertical_lines,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE))
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cntsv = cntsv[0] if len(cntsv) == 2 else cntsv[1]

for c in cnts:
    cv2.drawContours(frame,[c],-1,(255,255,255),2)

for c in cntsv:
    cv2.drawContour(frame,[c],-1,9255,255,255),2)
