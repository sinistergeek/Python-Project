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

def getNewBoard():
    return [['1','5','9','13'],['2','6','10','14'],['3','7','11','15'],['4','8','12',BLANK]]

def displayBoard(board):
    labels = [board[0][0],board[1][0],board[2][0],board[3][0],board[0][1],board[1][1],board[2][1],board[3][1],board[0][2],board[1][2],board[2][2],board[3][2],board[0][3],board[1][3],board[2][3],board[3][3]]
    boardToDraw = """
    +---+---+---+---+
     {}   {}  {}  {}
     {}   {}  {}  {}
     {}   {}  {}  {}
     {}   {}  {}  {}
    """.format(*labels)
    print(boardToDraw)


def findBlankSpace(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == ' ':
                return (x,y)


def askForPlayerMove(board):
    w = 'W'
    a = 'A'
    s = 'S'
    d = 'D'
    while True:
        print('     ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a,s,d))
        response = input('> ').upper()
        if response == 'QUIT':
