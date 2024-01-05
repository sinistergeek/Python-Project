import sys, random,time
try:
    import bext
except ImportError:
    print('This program request the bext module, which you')
    print('can still by following the instruction at')
    print('https://pypi.org/project/Bext')
    sys.exit()


WIDTH,HEIGHT = bext.size()
WIDTH -= 1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red','green','yellow'.'blue'.'magenta','cyan','white']
UP_RIGHT ='ur'
UP_LEFT = 'ul'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT,UP_LEFT,DOWN_RIGHT,DOWN_LEFT)
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()
    logos=[]
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR:random.choice(COLORS),
                      X: random_randint(1,WIDTH-4),
                      Y: random_randint(1,HEIGHT-4),
                      DIR:random.choice(DIRECTIONS)})

        if logos[-1][X] == 1:
            logos[-1][X] -= 1

    while True:
        for logo in logs:
            bext.goto(logo[X],logo[Y])
            print('     ',end='')

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1

            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = up_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1

            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif log[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            elif logo[Y]  == WIDTH - 3 and log[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == WIDTH -3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] - DOWN_RIGHT

            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)


            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1

            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1

            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1

            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

    bexts,goto(5,0)
    bext.fg('white')
    print('Corner bounces:',cornerBounces,end='')
    for logo in logos:
        bext.goto(logo[X],logo[Y])
        bext.fg(logo[COLOR])
        print('sinister',end='')
    bext.goto(0,0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD logo,by sinister')
        sys.exit()
