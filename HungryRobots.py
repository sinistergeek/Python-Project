import random,sys
WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS =100
EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'
WALL = chr(9617)
def main():
    print('''
    Hungry Robots, by sinistergeek You are trapped in a maze with hungry robots! You don't know why robots need to eat, but you don't want to find out. The robots are badly programmed and will move directly toward you, even if blocked by walls. You must trick the robots into crashing into each other (or dead robots) without being caught. You have a personal teleporter device, but it only has enough battery for {} strips. Keep in mind, you and robots can slip through the corners of two diagonal walls
    '''.format(NUM_TELEPORTS))
    input('Press Enter to begin...')
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition =  getRandomEmptySpace(board,robots)
    while True:
        displayBoard(board,robots,playerPosition)
        if len(robots) == 0:
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()
        playerPosition = askForPlayerMove(board,robots,playerPosition)
        robots =moveRobots(board,robots,playerPosition)
        for x,y in robots:
            if (x,y) == playerPosition:
                displayBoard(board,robots,playerPosition)
                print('You have been caught by a robot!')
                sys.exit()


def getNewBoard():
    board = {'teleports' : NUM_TELEPORTS}
    for x  in range(WIDTH):
        for y in range(HEIGHT):
            board[(x,y)] = EMPTY_SPACE
    for x in range(WIDTH):
        board[(x,0)] = WALL
        board[(x,HEIGHT - 1)] = WALL
    for y in range(HEIGHT):
        board[(0,y)] = WALL
        board[(WIDTH - 1, y)] = WALL

    for i in range(NUM_WALLS):
        x,y = getRandomEmptySpace(board,[])
        board[(x,y)] = WALL

    for i in range(NUM_DEAD_ROBOTS):
        x,y = getRandomEmptySpace(board,[])
        board[(x,y)] =DEAD_ROBOT
    return board

def getRandomEmptySpace(board,robots):
    while True:
        randomX = random.randint(1,WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX,randomY,board,robots):
            break
    return(randomX,randomY)

def isEmpty(x,y,board,robots):
    return board[(x,y)] == EMPTY_SPACE and (x,y) not in robots


def addRobots(board):
    robots = []
    for i in range(NUM_ROBOTS):
        x,y = getRandomEmptySpace(board,robots)
        robots.append((x,y))
    return robots

def displayBoard(board,robots,playerPosition):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if board[(x,y)] == WALL:
                print(WALL,end='')
            elif board[(x,y)] == DEAD_ROBOT:
                print(DEAD_ROBOT,end='')
            elif (x,y) == playerPosition:
                print(PLAYER,end='')
            elif (x,y) in robots:
                print(ROBOT,end='')
            else:
                print(EMPTY_SPACE,end='')
        print()
def askForPlayerMove(board,robots,playerPosition):
    playerX,playerY = playerPosition
    q = 'Q' if isEmpty(playerX - 1,playerY - 1,board,robots) else ' '
    w = 'W' if isEmpty(playerX + 0,playerY - 1,board,robots) else ' '
    e = 'E' if isEmpty(playerX + 1,playerY - 1,board,robots) else ' '
    d = 'D' if isEmpty(playerX + 1,playerY + 0,board,robots) else ' '
    c = 'C' if isEmpty(playerX + 1,playerY + 1,board,robots) else ' '
    x = 'X' if isEmpty(playerX + 0,playerY + 1,board,robots) else ' '
    z = 'Z' if isEmpty(playerX - 1,playerY + 1,board,robots) else ' '
    a = 'A' if isEmpty(playerX - 1,playerY + 0,board,robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S')
    while True:
        print('(T)eleports remaining: {}'.format(board["teleports"]))
        print('         ({})({})({})'.format(q,w,e))
        print('         ({})(S)({})'.format(a,d))
        print('Enter move or QUIT: ({}) ({}) ({})'.format(z,x,c))
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            board['teleports'] -= 1
            return getRandomEmptySpace(board,robots)
        elif move != '' and move in allMoves:
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX ,playerY)}[move]

def moveRobots(board,robotPositions,playerPosition):
    playerx,playery = playerPosition
    nextRobotPositions = []
    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]
        if robotx < playerx:
            movex = 1
        elif robotx > playerx:
            movex = -1
        elif robotx == playerx:
            movex = 0
        if roboty < playery:
            movey = 1
        elif roboty > playery:
            movey = -1
        elif roboty == playery:
            movey = 0
        if board[(robotx + movex,roboty + movey)] == WALL:
            if board[(robotx + movex,roboty)] == EMPTY_SPACE:
                movey = 0
            elif board[(robotx,roboty + movey)] == EMPTY_SPACE:
                movex = 0
            else:
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey
        if (board[(robotx,roboty)] == DEAD_ROBOT or board[(newRobotx,newRoboty)] == DEAD_ROBOT):
            del robotPositions[0]
            continue

        if (newRobotx, newRoboty) in nextRobotPositions:
            board[(newRobotx,newRoboty)] = DEAD_ROBOT
            nextRobotPositions.remove((newRobotx,newRoboty))
        else:
            nextRobotPositions.append((newRobotx,newRoboty))
        del robotPositions[0]
    return nextRobotPositions

if __name__ == '__main__':
    main()
