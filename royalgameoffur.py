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

        if flipTally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent
            continue
        validMoves = getValidMoves(gameBoard,turn,flipTally)
        if validMoves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent
            continue
        while True:
            print('Select move', flipTally,'spaces: ',end='')
            print(' '.join(validMoves) + 'quit')
            move = int('> ').lower()
            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in validMoves:
                break
            print('That is not a valid more.')
        if move == 'home':
            gameBoard[home] -= 1
            nextTrackSpaceIndex = flipTally
        else:
            gameBoard[move] = EMPTY
            nextTrackSpaceIndex = track.index(move) + flipTally

        movingOntoGoal = nextTrackSpaceIndex == len(track) - 1
        if movingOntoGoal:
            gameBoard[goal] += 1
            if gameBoard[goal] == 7:
                displayBoard(gameBoard)
                print(turn, 'has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            nextBoardSpace = track[nextTrackSpaceIndex]
            if gameBoard[nextBoardSpace] == opponent:
                gameBoard[opponentHome] += 1
            gameBoard[nextBoardSpace] = turn
        if nextBoardSpace in FLOWER_SPACES:
            print(turn,'landed on a flower space and goes again.')
            input('Press Enter to continue....')
        else:
            turn = opponent
