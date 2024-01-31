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
