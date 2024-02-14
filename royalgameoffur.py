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

def getNewBoard():
    board = {X_HOME: 7, X_GOAL: 0,O_HOME: 7,O_GOAL:0}
    for spaceLabel in ALL_SPACES:
        board[spaceLabel] = EMPTY
    return board

def displayBoard(board):
    print('\n' * 60)

    xHomeTokens = ('X' * board[X_HOME]).ljust(7,'.')
    xGoalTokens = ('X' * board[X_GOAL]).ljust(7,'.')
    oHomeTokens = ('O' * board[O_HOME]).ljust(7,'.')
    oGoalTokens = ('O' * board[O_GOAL]).ljust(7,'.')
    spaces = []
    spaces.append(xHomeTokens)
    spaces.append(xGoalTokens)
    for spaceLabel in ALL_SPACES:
        spaces.append(board[spaceLabel])
    spaces.append(oHomeTokens)
    spaces.append(oGoalTokens)
    print(BOARD_TEMPLATE.format(*spaces))

def getValidMoves(board,player,flipTally):
    validMoves = []
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAyEr:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME
    if board[home] > 0 and board[track[flipTally]] == EMPTY:
        validMoves.append('home')

    for trackSpaceIndex,space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue
        nextTrackSpaceIndex = trackSpaceIndex + flipTally
        if nextTrackSpaceIndex >= len(track):
            continue
        else:
            nextBoardSpaceKey = track[nextTrackSpaceIndex]
            if nextBoardSpaceKey == 'G':
                validMoves.append(space)
                continue
        if board[nextBoardSpaceKey] in (EMPTY,opponent):
            if nextBoardSpaceKey == '1' and board['1'] == opponent:
                continue
            validMoves.append(space)
    return validMoves

if __name__ == '__main__':
    main()
