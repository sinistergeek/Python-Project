import random,sys

BLANK = ' '
def main():
    print('''
    Sliding Tile Puzzle Use the WASD keys to move the tiles back into their original order
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15
    ''')
    input('Press Enter to begin...')
    gameBoard = getNewPuzzle()
    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)
        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()
