import random, shutil, sys, time
PAUSE = 0.2
DENSITY = 0.10
DUCKLING_WIDTH=5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

def main():
    print('Duckling Screensaver')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)
    while True:
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            if (ducklingObj == None and random.random() <= DENSITY):
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj
            if ducklingObj != None:
                print(ducklingObj.getNextBodyPart(),end='')
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None

            else:
                print(' '* DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

class Duckling:
    def __init__(self):
        self.direction =  random.choice([LEFT,RIGHT])
        self.body = random.choice([CHUBBY,VERY_CHUBBY])
        self.mouth = random.choice([OPEN,CLOSED])
        self.wing = random.choice([OUT,UP,DOWN])
        if self.body = CHUBBY:
            self.eyes = BEADY

        else:
            self.eyes = random.choice([BEADY,WIDE,HAPPY,ALOOF])
