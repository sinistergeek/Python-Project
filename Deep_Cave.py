import random, sys, time
WIDTH = 70
PAUSE_AMOUNT = 0.05
print('Deep Cave,by sinistergeek')
print('Press Ctrl-C to stop.')
time.sleep(2)
leftWidth = 20
gapWidth = 10
while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#'*leftWidth) + (' '* gapWidth) + ('#'*rightWidth))
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyBoardInterrupt:
        sys.exit()
    diceRolll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth == 1 and leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass

            

