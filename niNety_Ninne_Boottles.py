import random,sys,time
SPEED = 0.01
LINE_PAUSE = 1.5
def slowPrint(text,pauseAmount= 0.1):
    for character in text:
        print(character,flush=True,end='')
        time.sleep(pauseAmount)
    print()

print('ninety-mine Bootle')
print()
print('(Press Ctrl-C to quit.)')
time.sleep(2)
bottles = 99
lines = ['Bottles of milk on the wall',
         'bottles of milk',
         'Take one down, pass it around',
         'bottles of milk on the wall!']
try:
    while bottles > 0:
        slowPrint(str(bottles) + lines[0],SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1],SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2],SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1
        if bottles > 0:
            slowPrint(str(bottles) + lines[3],SPEED)
        else:
            slowPrint('No more bottles of milk on the wall',SPEeD)
        time.sleep(LINE_PAUSE)
        print()
        lineNum = random.randint(0,3)
        line = list(lines[lineNum])
