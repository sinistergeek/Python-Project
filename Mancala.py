import sys

PLAYER_1_PITS = ('A','B','C','D','E','F')
PLAYER_2_PITS = ('G','H','I','J','K','L')

OPPOSITE_PIT = {'A':'G','B':'H','C':'I','D':'J','E':'K','F':'L','G':'A','H':'B','I':'C','J':'D','K':'E','L':'F'}

NEXT_PIT = {'A':'B','B':'C','C':'D','D':'E','E':'F','F':'1','1':'L','L':'K','K':'J','J':'I','I':'H','H':'G','G':'2','2':'A'}

PIT_LABELS = 'ABCDEF1LKJIHG2'
STARTING_NUMBER_OF_SEEDS = 4

def main():

    print('''
      Mancala,The ancient two-player send-sowing game. Grab the seeds from a pit on your side and place one in each following pit, going counterclockwise and skipping your opponent's store. If your last seed lands in a empty pit of yours, move the opposite pit's seeds into that pit. The goal is to get the most seeds in your store on the side of the board. If you last paced seed is in yopur store, you get a free turn. The game ends when all of one player's pits are empty. The other player claims the remaining seeds for their store, and the winner is the one with most seeds.
''')
    input('Press Enter to begin....')
    gameBoard = getNewBoard()
    playerTurn = '1'
    while True:
        print('\n'* 60)
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn,gameBoard)
        playerTurn = makeMove(gameBoard,playerTurn,playerMove)
        winner = checkForWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)
            print('Player' + winner + 'has won!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)
            print('There is a tie!')
            sys.exit()

def getNewBoard():
    s = STARTING_NUMBER_OF_SEEDS
    return {'1':0,'2':0,'A':s,'B':s,'C':s,'D':s,'E':s,'F':s,'G':s,'H':s,'I':s,'J':s,'K':s,'L':s}

def displayBoard(board):
    seedAmounts = []

    for pit in 'GHIJKL21ABCDEF':
        numSeedsInThisPit = str(board[pit]).rjust(2)
        seedAmounts.append(numSeedsInThisPit)
        print("""
        +---------+---------+--------+-----+---------+
        G{} | H{} |I{} | J{}| K{} | L{}
        A{} | B{} |C{} | D{}| E{} | F{}
        +---------+---------+--------+-----+---------+
        """.format(*seedAmounts))

