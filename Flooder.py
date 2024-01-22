import random,sys
try:
    import bext
except ImportError:
    print('This requires the bext module')
    sys.exit()


BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME =20
HEART = chr(9829)
DIAMOND = chr(9830)
SPADE =chr(9824)
BALL = chr(9679)
TRIANGLE = chr(9650)

BLOCK = chr(9608)
LEFTRIGHT = chr(9472)
UPDOWN = chr(9474)
DOWNRIGHT = chr(9484)
DOWNLEFT = chr(9488)
UPRIGHT = chr(9892)
UPLEFT = chr(9496)

TILE_TYPES =(0,1,2,3,4,5)
COLORS_MAP = {0:'red',1:'green',2:'blue',3:'yellow',4:'cyan',5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0:HEARt,1:TRIANGLE,2:DIAMOND,3:BALL,4:CLUB,5:SPADE}
SHAPE_MODE = 'shape mode'
def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE
    gameBoard = getNewBoard()
    movesLeft = MOVEs_PER_GAME
    while True:
        displayBoard(gameBoard, displayMode)
        print('Moves left:',movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard,0,0)
        movesLeft -= 1
        if hasWond(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard,displayMode)
            print('You have run out of moves!')
            break

def getNewBoard():
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x,y)] = random.choice(TILE_TYPES)
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0,BOARD_HEIGHT - 1)
    return board
