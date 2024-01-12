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
