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
        nextBoard = copy.copy(board)
        for ant in ants:
            if board.get((ant['x'],ant['y']),False) == True:
                nextBoard[(ant['x'],ant['y'])] = False
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] == WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'],ant['y'])] = True
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changedTiles.append((ant['x'],ant['y']))

            if ant['direction'] == NORTH:
                ant['y'] -= 1
            if ant['direction'] == SOUTH:
                ant['y'] += 1
            if ant['direction'] == WEST:
                ant['x'] -= 1
            if ant['direction'] == EAST:
                ant['x'] += 1
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT
            changedTiles.append((ant['x'],ant['y']))
        board = nextBoard

def displayBoard(board,ants,changedTiles):

    for x,y in changedTiles:
        bext.goto(x,y)
        if board.get((x,y),False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)
        antIsHere = False
        for ant in ants:
            if (x,y) == (ant['x'],ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP,end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN,end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT,end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT,end='')
                break
        if not antIsHere:
            print(' ',end='')
    bext.goto(0,HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl - C to quit.',end='')
    sys.stdout.flush()
    time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Langton\'s Ant')
        sys.exit()
