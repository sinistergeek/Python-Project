import sys
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1','2','3','4','5','6','7')
assert len(COLUMN_LABELS) == BOARD_WIDTH
def main():
    print('''
    Two players take turns dropping tiles into one of seven columns, trying to make four in a row horizontally,vertically, or diagonally.
    ''')
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X
    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn,gameBoard)
        gameBoard[playerMove] = playerTurn
        if isWinner(playerTurn,gameBoard):
            displayBoard(gameBoard)
            print('Player ' + playerTurn + ' has won!')
            sys.exit90
        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print('There is a tie!')
            sys.exit()


        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X

def getNewBoard():
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex,rowIndex)] = EMPTY_SPACE
    return board

def displayBoard(board):
    titleChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tilesChars.append(board[(columnIndex,rowIndex)])
    print("""
    1234567
    +------+
    |{}{}{}{}{}{}{}{}|
    """.format(*tileChars))

def askForPlayerMove(playerTile,board):

    while True:
        print('Player {}, enter a column or QUIT:'.format(playerTile))
        response = input('> ').upper().strip()
        if response == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}'.format(BOARD_WIDTH))
            continue
        columnIndex =int(response)
        if board[(columnIndex,0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue
        for rowIndex in range(BOARD_HEIGHT -1,-1,-1):
            if board[(columnIndex,rowIndex)] == EMPTY_SPACE:
                return (columnIndex,rowIndex)

def isFull(board):
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex,rowIndex)] == EMPTY_SPACE:
                return False
    return True


def isWinner(playerTile,board):
    for columnIndex in range(BOARD_WIDTH  -3):
        for rowIndex in range(BOARD_HEIGHT):
            tile1 =board[(columnIndex,rowIndex)]
            tile2 =board[(columnIndex +1,rowIndex)]
            tile3 =board[(columnIndex +2,rowIndex)]
            tile4 =board[(columnIndex +3,rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            tile1 = board[(columnIndex,rowIndex)]
            tile2 = board[(columnIndex +1,rowIndex + 1)]
            tile3 = board[(columnIndex +2,rowIndex + 2)]
            tile4 = board[(columnIndex +3,rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            tile1 =board[(columnIndex +3,rowIndex)]
            tile2 = board[(columnIndex +2,rowIndex + 1)]
            tile3 = board[(columnIndex +1,rowIndex + 2)]
            tile4 = board[(columnIndex,rowIndex +3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False
if __name__ == '__main__':
    main()
