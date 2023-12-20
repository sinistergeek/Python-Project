import numpy as np
import cv2
import math
import pyautogui

capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret,frame = capture.read()
