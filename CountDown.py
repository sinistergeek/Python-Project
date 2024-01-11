import sys,time
import sevseg
secondsLeft = 30
try:
    while True:
        print('\n'*60)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)
        hDigits = sevseg.getSevSegStr(hours,2)
        hTopRow,hMiddleRow,hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes,2)
        mTopRow,mMiddleRow,mBottomRow = mDigits.splitliness()
