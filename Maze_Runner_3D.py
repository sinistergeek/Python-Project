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

def pasteWallDict(srcWallDict,dstWallDict,left,top):
    dstWallDict = copy.copy(dstWallDict)
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left,y + top)] = srcWallDict[(x,y)]
    return dstWallDict

def makeWallDict(maze,playerx,playery,playerDirection,exitx,exity):
    if playerDirection == NORTH:
        offsets = (('A',0,-2),('B',-1,-1),('C',0,-1),('D',1,-1),('E',-1,0),('F',1,0))

    if playerDirection == SOUTH:
        offsets = (('A',0,2),('B',1,1),('C',0,-1),('D',1,-1),('E',-1,0),('F',1,0))
    
    if playerDirection == EAST:
        offsets = (('A',2,0),('B',1,-1),('C',1,0),('D',1,1),('E',0,-1),('F',0,1))
    
    if playerDirection == WEST:
        offsets = (('A',-2,0),('B',-1,1),('C',-1,0),('D',-1,-1,),('E',0,1),('F',0,-1))

    section = {}
    for sec,xOff, yOff in offsets:
        section[sec] = maze.get((playerx + xOff,playery + yOff),WALL)
        if(playerx + xOff,playery + yOff) == (exitx,exity):
            section[sec] = EXIT

    wallDict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {'A':(6,4),'B':(4,3),'C':(3,1),'D':(10,3),'E':(0,0),'F':(12,0)}

