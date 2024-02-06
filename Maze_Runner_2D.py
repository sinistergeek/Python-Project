import sys, os

WALL = '#'
EMPTY = ''
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617)

def displayMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x,y) == (playerx,playery):
                print(PLAYER,end='')

            elif (x,y) == (exitx,exity):
                print('X',end='')
            elif maze[(x,y)] == WALL:
                print(BLOCK,end='')
            else:
                print(maze[(x,y)],end='')
        print()
print('''
MAze Runner 2D
      ''')
while True:
    print('Enter the filename of the maze(or list or Quit)')
    filename = input('> ')
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for fileInCurrentFolder in os.getcwd():
            if(fileInCurrentFolder.startswith('maze') and fileInCurrentFolder.endswith('.txt')):
                print(' ',fileInCurrentFolder)
        continue
    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file name',filename)

mazefile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0

for line in lines:
    WIDTH = len(line.rstrip())
    for x,character in enumerate(linerstrip()):
        assert character in (WALL,EMPTY,START,EXIT),'Invalid character at column {},line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x,y)] = character
        elif character == START:
            playerx,playery = x,y
            maze[(x,y)] = EMPTY
        elif character == EXIT:
            exitx,exity = x,y
            maze[(x,y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None,'No start in maze file.'
assert exitx != None and exity != None, 'No exit in maze file.'

While True:
    displayMaze(maze)
    while True:
        print('         W')
        print('Enter direction, or QUIT: ASD')
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if move not in ['W','A','S','D']:
            print('Invalid direction. Enter one of W,A,S, or D')
            continue

        if move == 'W' and maze[(playerx,playery - 1)] == EMPTY:
            break
        if move == 'S' and maze[(playerx,playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break
        print('You cannot move in that direction')

    if move == 'W':
        while True:
            player -= 1
            if (playerx,playery - 1) == (exitx,exity):
                break
            if maze[(playerx,playery - 1)] == WALL:
                break
            if (maze[(playerx + 1, playery)]== EMPTY):
                break
    elif move == 'S':
        while True:
            playery += 1
            if (playerx,playery) == (exitx,exity):
                break
            if maze[(playerx,playery + 1)] == WALL:
                break
            if (maze[(playerx - 1, playery)]) == EMPTY or maze[(playerx + 1, playery)] == EMPTY):
                break
    elif move == 'A':
        while True:
            if (playerx,playery) == (exitx,exity):
                break
            if maze[(playerx - 1,playery)] == WALL:
                break
            if (maze[(playerx,playery - 1)] == EMPTY
                or maze[(playerx,playery + 1)] == EMPTY):
                break

    elif move == 'D':
        while True:
            playerx += 1
            if (playerx,playery) == (exitx,exity):
                break
            if maze[playerx + 1,playery] == WALL:
                break
            if (maze[(playerx,playery - 1)] == EMPTY or maze[(playerx,playery + 1)]==EMPTY):
                break

    if(playerx,playery) == (exitx,exity):
        displayMaze(maze)
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
