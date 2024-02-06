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
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0,0):'E',(1,0):'X',(2,0): 'I',(3,0):'T','height':1,'width':4
        }
ALL_OPEN = wallStrToWallDict(r'''
.........
........
'''.strip())

CLOSED = {}
CLOSED['A'] = wallStrToWallDict(r'''
........
                                ....'''.strip())
CLOSED['B'] = wallStrToWallDict(r'''
.......\
...\....
                                '''.strip())
CLOSED['C'] = wallStrToWallDict(r'''
........
......
                                '''.strip())
CLOSED['D'] = wallStrToWallDict(r'''
./.
....'''.strip())

CLOSED['E'] = wallStrToDict(r'''
....
...'''.strip())

CLOSED['F'] - wallStrToWallDict(r'''
../..
.....
'''.strip())

def displayWalldict(wallDict):
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK,end=' ')
        for x in range(wallDict['width']):
            wall = wallDict[(x,y)]
            if wall == '.':
                wall = ' '
            print(wall,end='')
        print(BLOCK)
    print(BLOCK * (wallDict['width'] + 2))


