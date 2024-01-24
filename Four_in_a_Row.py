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
