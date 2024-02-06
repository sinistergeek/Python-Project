import copy,sys,os

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'

def wallStrToWallDict(wallStr):
    wallDict = {}
    height = 0
    width = 0
    for y,line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
        for x,character in enumerate(line):
            if x > width:
                width = x
            wallDict[(x,y)] = character
    wallDict['height'] = height + 1
