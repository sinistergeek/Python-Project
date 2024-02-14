import random,sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

ALL_SPACEs = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghjklmnopstG'
O_TRACK = 'HabcdijklmnopqrG'

FLOWEr_SPACES = ('h','t','l','d','r')

BOARD_TEMPLATE = """
{}      {}
{} < {} < {} < {} |     |{} < {}
{} > {} > {} > {} > {} > {} > {} > {}
{} < {} < {} < {} < {} |  {} < {}
home    Goal
{}      {}
"""

def main():
    print('''
    The Royal Game of Ur,
    This is a 5,000 year old game. Two players must move their tokens from their home to their goal. On your turn you flip four coins and can move one token a number of spaces equal to the heads you got. Ur is a racing game; the first player to move all seven of their tokens to their goal wins. To do this, tokens must travel from their home to their goal
    ''')
    input('Press Enter to begin....')
    gameBoard = getNewBoard()
    turn = O_PLAYER
    while True:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponentHome = O_HOME
        elif turn == O_PLAYER:
            opponent =X_PLAYER
            home = O_PLAYER
            track = O_TRACK
            goal = O_GOAL
            opponentHome = X_HOME
        displayBoard(gameBoard)
        input('It is' + turn + '\'s turn. Press Enter to flip...')

        flipTally = 0
        print('Flips: ',end='')
        for i in range(4):
            result = random.randint(0,1)
            if result == 0:
                print('T',end='')
            else:
                print('H',end='')
            if i != 3:
                print('-',end='')
            flipTally += result
        print(' ',end='')
