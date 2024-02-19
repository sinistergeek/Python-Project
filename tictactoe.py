ALL_SPACES = ['1','2','3','4','5','6','7','8','9']
X, O, BLANK = 'X','O',' '
def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O
    while True:
        print(getBoardStr(gameBoard))
        move = None
        while not isValidSpace(gameBoard,move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard,move,currentPlayer)
        if isWinner(gameBoard,currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')

def getBlankBoard():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board

def getBoardStr(board):
    return '''
    {}|{}|{} 1 2 3
    -+-+-
    {}|{}|{} 4 5 6
    -+-+-
    {}|{}|{} 7 8 9
    '''.format(board['1'],board['2'],board['3'],
               board['4'],board['5'],board['6'],
               board['7'],board['8'],board['9'])

def isValidSpace(board,space):
    return space in ALL_SPACES and board[space] == BLANK

