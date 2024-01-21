import random, sys, time
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    sys.exit()

WIDTH, HEIGHT =bext.size()
WIDTH -= 1
NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 4
FISH_TYPES =[
    {'right':['><>'],       'left':['<><']},
    {'right':['>||>'],      'left':['<||<']}
        ]
LONGEST_FISH_LENGTH =10
TOP_EDGE = 0
BOTTOM_EDGE =HEIGHT - 2
