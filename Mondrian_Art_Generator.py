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

