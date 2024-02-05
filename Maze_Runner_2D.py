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
