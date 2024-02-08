import sys, time
print('Ninety-Nine Bottles')
print()
print('(Press Ctrl-C to quit.)')
time.sleep(2)
bottles = 99
PAUSE = 2
try:
    while bottles > 1:
        print(bottles,'bottles of milk on the wall.')
        time.sleep(PAUSE)
        print(bottles,'bottles of milk')
        time.sleep(PAUSE)
        print('Take one down, pass it around')
        time.sleep(PAUSE)
        bottles = bottles - 1
        print(bottles,'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()
    print('1 bottle of milk on the wall.')
    time.sleep(PAUSE)
    print('1 bottle of milk')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles, pass it around')
except KeyboardInterrupt:
    sys.exit()
