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

def main():
    global FISHES, BUBBLERS,BUBBLES,KELPS,STEP
    bext.bg('black')
    bext.clear()
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    BUBBLES = []
    for i in range(NUM_BUBBLERS):
        BUBBLERS.append(random.randint(LEFT_EDGE,RIGHT_EDGE))
    BUBBLES = []
    KEkps = []
    for i in range(NUM_KElP):
        kelpx = random.randint(LEFT_EDGE,RIGHT_EDGE)
        Kelp = {'x':kelpx,'segments':[]}
        for i in range(random.randint(6,HEIGHT -1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1/FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1

def getRandomColor():
    return random.choice(('black','red','green','yellow','blue','purple','cyan','white'))

def generateFish():
    fishType =random.choice(FISH_TYPES)
    colorPattern =random.choice(('random','head-tail','single'))
    fishLength = len(fishType['random'][0])
    if colorPattern == 'random':
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        color = [getRandomColor()]
    if colorPattern == 'head-tail':
        headTailColor = getRandomColor()
        colors[0] = headTailColor
        colors[-1] = headTailColor

    fish = {'right':            fishType['right'],
            'left':             fishType['left'],
            'colors':           colors,
            'hSpeed':           random.randint(1,6),
            'vSpeed':           random.randint(5,15),
            'timeToHDirChange': random.randint(10,60),
            'timeToVDirChange': random.randint(2,20),
            'goingRight':       random.choice([True,False]),
            'goingDown':        random.choice([True,False])
            }
    fish['x'] = random.randint(0,WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0,HEIGHT - 2)

def simulateAquarium():
    global FISHES,BUBBLERS,BUBBLES,KELP,STEP
    for fish in FISHES:
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1
                else:
                    fish['goingRight'] = False
                    fish['colors'].reverse()
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1
                else:
                    fish['goingRight'] = True
                    fish['colors'].reverse()
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10,60)
            fish['goingRight'] = not fish['goingRight']
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1
                else:
                    fish['goingDown'] =  False
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1
                else:
                    fish['goingDown'] = True
        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToDirChange'] = random.randint(2,20)
            fish['goingDown'] = notFish['goingDown']
    for bubbler in BUBBLERS:
        if random.randint(1,5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    for bubble in BUBBLES:
        diceRoll = random.randint(1,6)
        if(diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1
        elif(diceRoll == 2):
            bubble['x'] += 1
        bubble['y'] -= 1

    for i in range(len(BUBBLES) -1, -1,-1):
        if BUBBLES[i]['y'] == TOP_EDGE:
            del BUBBLES[i]

    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if random.randint(1,20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def drawAquarium():
    bext.fg('white')
    bext.goto(0,0)
    print('Fish tank, by sinister geek Ctrl-C quit.',end='')

