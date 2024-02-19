ALL_SPACES = ['1','2','3','4','5','6','7','8','9']
X, O, BLANK = 'X','O',' '
def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O
    while True:
        print(getBoardStr(gameBoard))

