import cv2
import numpy as np
def make_points(image,line):
    slope,intercept = line
    y1 = int(image.shape[0])
    y2 = int(y1 * 3/5)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1,y1,x2,y2]]


def average_slope_intercept(image,lines):
    left_fit = []
    right_fit = []
    if lines is None:
        return None

