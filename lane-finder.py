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
    for line in lines:
        for x1,y1,x2,y2 in line:
            fit = np.polyfit((x1,x2),(y1,y2),1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:
                left_fit.append((slope,intercept))
            else:
                right_fit.append((slope,intercept))

    left_fit_average = np.average(left_fit,axis=0)
    right_fit_average = np.average(right_fit,axis=0)
    left_line = make_points(image,left_fit_average)
    right_line = make_points(image,right_fit_average)
    averaged_linmes = [left_line,right_line]

    return averaged_lines

