import random,sys,time
print('Fast Draw, by sinistergeek')
print()
print('Time to test your reflexes and see if you are the fastest')
print('draw in the west!')
print('When you see "DRAW",you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
input('Press Enter to begin...')
while True:
    print()
    print('It is high noon....')
    time.sleep(random.randint(20,50)/10.0)
    print('DRAW!')
    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime
    if timeElapsed < 0.01:
        print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You took',timeElapsed, 'seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed,4)
        print('You took',timeElapsed, 'seconds to draw.')
        print('You are the fastest draw in the west! You win!')
    print('Enter QUIT to stop, or press Enter to play again.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
