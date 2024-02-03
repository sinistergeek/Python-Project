import copy, random, sys,time
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
HEIGHT -= 1
NUMBER_OF_ANTS = 10
PAUSE_AMOUNT = 0.1
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

ANT_COLOR = 'red'
BLACK_TITLE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

def main():
    bext.fg(ANT_COLOR)
    bext.bg(WHITE_TILE)
    bext.clear()

    board = {'width':WIDTH,'height':HEIGHT}

    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
                'x': random.randint(0,WIDTH - 1),
                'y': random.randint(0,HEIGHT - 1),
                'direction': random.choice([NORTH,SOUTH,EAST,WEST])
                }
        ants.append(ant)
    changedTiles = []
    while True:
        displayBoard(board,ants,changedTiles)
        changedTiles = []
