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

