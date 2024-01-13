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

D6a = ([
    '+------+',
    '|O    O|',
    '|O    O|',
    '|O    O|'
    ],6)

D6b = ([
    '+------+',
    '|O O O |',
    '|      |',
    '|O O O |'],6)

ALL_DICE = [D1,D2a,D2b,D3a,D3b,D4,D5,D6a,D6b]
print('''
      Dice Math, by sinstergeek
      Add up  the sides of all the dice displayed on the screen. You have {} seconds to answer as many as possible. You get {} points for each correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION,REWARD,PLENTY))
input('Press Enter to begin....')

correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MID_DICE,MAX_DICE)):
        die = random.choice(ALL_DICE)
        diceFaces.append(die[0])
        sumAnswer += die[1]
    topLeftDiceCorners = []
    for i in range(len(diceFaces)):
        while True:
            left = random.randint(0,CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0,CANVAS_HEIGHT - 1 - DICE_HEIGHT)

