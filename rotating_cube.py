import math, time, sys, os

PAUSE_AMOUNT = 0.1
WIDTH,HEIGHT = 80,24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2
LINE_CHAR = chr(9608)

X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

X = 0
Y = 1
Z = 2

def line(x1,y1,x2,y2):
    points = []
