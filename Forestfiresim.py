import random, sys, time
try:
    import bext

except ImportError:
    print('This program requires the bext module')
    sys.exit()

WIDTH = 79
HEIGHT = 22
TREE = 'A'
FIRE = 'W'
EMPTY = ' '
INITAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5

def main():
    forest = createNewForest()
    bext.clear()
    while True:
        displayForest(forest)
        nextForest = {'width':forest['width'],'height':forest['height']}
        for x in range(forest['width']):
            for y in range(forest['height']):
                if(x,y) in nextForest:
                    continue
                if ((forest[(x,y)] == EMPTY) and (random.random() <= GROW_CHANCE)):
                    nextForest[(x,y)] = TREE
                elif ((forest[(x,y)] == TREE) and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x,y)] FIRE
                elif forest[(x,y)] == FIRE:
                    for ix in range(-1,2):
                        for iy in range(-1,2):
                            if forest.get((x + ix,y + iy)) == TREE:
                                nextForest[(x + ix,y + iy)] = FIRE
                    nextForest[(x,y)] = EMPTY
                else:
                    nextForest[(x,y)] = forest[(x,y)]


