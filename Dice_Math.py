import random,time
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6
REWARD = 4
PENALTY = 1
assert MAX_DICE <= 14
D1 = ([
    '+------+',
    '|      |',
    '|  0   |',
    '|      |',
    '+------+'
    ],1)
D2a = ([
    '+------+',
    '| O    |',
    '|      |',
    '|     O|',
    '+------+'
    ],2)
D2b =([
    '+------+',
    '|     O|',
    '|      |',
    '|O     |',
    '+------+',
    ],2) 
D3a = ([
    '+------+',
    '|O     |',
    '|   O  |',
    '|     O|',
    ],3)
D3b = ([
    '+------+',
    '|     O|',
    '|   O  |',
    '|O     |'
    ],3)

D4 = ([
    '+------+',
    '|O    O|',
    '|      |',
    '|O    O|'
    ],4)

D5 = ([
    '+------+',
    '|O    O|',
    '|   O  |',
    '|O    O|'
    ],5)
