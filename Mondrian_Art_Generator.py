import sys, random
try:
    import bext
except ImportError:
    print('This program requires the bext module')
    sys.exit()

MIN_X_INCREASE = 6
MIN_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

width,height = bext.size()
width -= 1
height -= 3
while True:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x,y)] = WHITE
    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE,MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            canvas[(x,y)] = BLACK
        x += random.randint(MIN_X_INCREASE,MAX_X_INCREASE)
    y = random.randint(MIN_Y_INCREASE,MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            canvas[(x,y)] = BLACK
        y += random.randint(MIN_Y_INCREASE,MAX_Y_INCREASE)
    numberOfRectanglesToPoint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)
    for i in range(numberOfSegmentsToDelete):
        while True:
            startx = random.randint(1,width - 2)
            starty = random.randint(1,height -2)
            if canvas[(startx,starty)] == WHITE:
                continue
            elif (canvas[(startx,starty - 1)] == WHITE and canvas[(startx,starty + 1)] == WHITE):
                orientation = 'horizontal'
            else:
                continue
            pointsToDelete = [(startx,starty)]
            canDeleteSegment = True
            if orientation == 'vertical':
                for changey in (-1,1):
                    y = starty
                    while 0 < y < height -1:
                        y += changey
                        if (canvas[(startx - 1,y)] == BLACK and canvas[(startx + 1,y)] == BLACK):
                            break
                        elif((canvas[(startx -1, y)] ==WHITE and canvas[(startx + 1,y)] = BALCK) or (canvas[(startx - 1,y)] == BLACK and canvas[(startx + 1, y)] == WHITE)):
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx,y))
            elif orientation == 'horizontal':
                for changex in (-1,1):
                    x = startx
                    while 0 < x < width - 1:
                        x += changex
                        if(canvas[(x,starty -1)] == BLACK and canvas[(x,starty + 1)] == BLACK):
                            break
                        elif((canvas[(x,starty -1)] == WHITE and canvas[(x,starty + 1)] == BLACK) or (canvas[(x,starty - 1)] == BLACK and canvas[(x,starty + 1)] =WHITE)):
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx,starty))

            if not canDeleteSegment:
                continue
            break
        for x,y in pointsToDelete:
            canvas[(x,y)] = WHITE
    for x in range(width):
        canvas[(x,0)] = BLACK
        canvas[(x,height - 1)] = BLACK
    for y in range(height):
        canvas[(0,y)] = BLACK
        canvas[(width -1,y)]

    for i in range(numberOfRectanglesToPaint):
        while True:
            startx = random.randint(1,width - 2)
            starty = random.randint(1,height - 2)
            if canvas[(startx,starty)] != WHITE:
                continue
            else:
                break

        colorToPaint = random.choice([RED,YELLOW,BLUE,BLACK])
        pointsToPaint = set([(startx,starty)])
        while len(pointsToPaint) > 0:
            x,y = pointsToPaint.pop()


