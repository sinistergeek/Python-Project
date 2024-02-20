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
        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()

def getNewBoard():

    newBoard = {}
    for x in range(4):
        for y in range(4):
            newBoard[(x,y)] = BLANK
    startingTwosPlaced = 0
    while startingTwosPlaced < 2:
        randomSpace = (random.randint(0,3),random.randint(0,3))
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1
    return newBoard

def drawBoard(board):
    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x,y)]
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)
    print("""
    +----+-----+----+---+
    {}|{} {}|{}
    {}|{} {}|{}
    {}|{} {}|{}
    {}|{} {}|{}
    +----+-----+----+----+
    """.format(*labels))


def getScore(board):
    score = 0 
    for x in range(4):
        for y in range(4):
            if board[(x,y)] != BLANK:
                score = score + board[(x,y)]
    return score

def combineTilesInColumn(column):
    combinedTiles = []
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)
    for i in range(3):
        if combinedTiles[i] == combinedTiles[i + 1]:
            combinedTiles[i] *= 2
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK
    return combinedTiles
