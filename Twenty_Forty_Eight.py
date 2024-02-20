import random, sys

BLANK = ''

def main():
    print('''
    Twenty Forty-Eight, Slide all the tiles on the board in one of four directions. Tiles with like numbers will combine into larger-numbered tiles. A new 2 tile is added to the board on each move. You win if you can create a 2048 tile. You lose if the board fills up the tiles before then.
    ''')
    input('Press Enter to begin...')
    gameBoard = getNewBoard()
    while True:
        drawBoard(gameBoard)
        print('Score:',getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard,PlayerMove)
        addTwoBoard(gameBoard)
