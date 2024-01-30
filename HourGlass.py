import random, sys,time
try:
    import bext
except ImportError:
    print('This require bext module')
    sys.exit()

PAUSE_LENGTH = 0.2
WIDE_FALL_CHANCE = 50
SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0
Y = 1
SAND = chr(9617)
WALL = chr(9608)
HOURGLASS = set()
for i in range(18,37):
    HOURGLASS.add((i,1))
    HOURGLASS.add((i,23))
for i in range(1,5):
    HOURGLASS.add((18,i))
    HOURGLASS.add((36,i))
    HOURGLASS.add((18,i + 19))
    HOURGLASS.add((36,i + 19))

for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))
    HOURGLASS.add((35 - i, 5 + i))
    HOURGLASS.add((25 - i, 13 + i))
    HOURGLASS.add((29 + i, 13 + i))

INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x,y + 4))
def main():
    bext.fg('yellow')
    bext.clear()
    bext.goto(0,0)
    print('Ctrl - C to quit',end='')
    for wall in HOURGLASS:
        bext.goto(wall[x],wall[Y])
        print(WALL,end='')
    while True:
        allSand = list(INITIAL_SAND)
        for sand in allSand:
            bext.goto(sand[X],sand[Y])
            print(SAND,end='')
        runHourglassSimulation(allSand)

def runHourglassSimulation(allSand):
    while True:
        random.shuffle(allSand)
        sandMoveOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                continue
            noSandBelow = (sand[X],sand[Y] + 1) not in allSand
            noWallBelow = (sand[X],sand[Y] + 1) not in HOURGlASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                bext.goto(sand[X],sand[Y])
                print(' ',end='')
                bext.goto(sand[X],sand[Y] + 1)
                print(SAND,end='')
                allSand[i] = (sand[X],sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                belowLeft = (sand[X] -1,sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1,sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft and noWallLeft and notOneLeftEdge)
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1,sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and noWallBeloRight and noWallRight and notOnRightEdge)

