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
