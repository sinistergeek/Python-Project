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

    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1,y1),(x2,y2)]
    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        x1,y1 = y1,x1
        x2,y2 = y2,x2
    isReversed = x1 > x2
    if isReversed:
        x1, x2 = x2,x1
        y1, y2 = y2,y1
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        for currentx in range(x2,x1-1,-1):
            if isSteep:
                points.append((currenty,currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:
                currenty -= ydirection
                extray += deltax
    else:
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1

        for currentx in range(x1,x2+1):
            if isSteep:
                points.append((currenty,currentx))
            else:
                points.append((currentx,currenty))
            extray -= deltay
            if extray < 0:
                currenty +=ydirection
                extray += deltax
    return points
def rotatePoint(x,y,z,ax,ay,az):
    rotatedX = X
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x,y,z = rotatedX,rotatedY,rotatedZ
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z
    return (rotatedX,rotatedY,rotatedZ)

def adjustPoint(point):
    return (int(point[X] * SCALEX + TRANSLATEX), int(point[Y] * SCALEY + TRANSLATEY))

CUBE_CORNERS = [[-1,-1,-1],[1,-1,-1],[-1,-1,1],[1,-1,1],[-1,1,-1],[1,1,-1],[-1,1,1],[1,1,1]
        ]

