import sys, time
import sevseg
try:
    while True:
        print('\n'*60)
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'

        minutes = str(currentTime.tm_tm_min)
        seconds = str(currentTime.tm_sec)
        hDigits = sevseg.getSevStr(hours,2)
        hTopRow,hMiddleRow,hBottomRow =hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes,2)
        mTopRow,mMiddleRow,mBottomRow = mDigits.splitlines()
        sDigits =sevseg.getSevSegStr(seconds,2)
        sTopRow,sMiddleRow,sBottomRow = sDigits.splitlines()
        print(hTopRow + '       ' + mTopRow + '     '+sTopRow)
        print(hMiddleRow + '    *    ' + mMiddleRow + '     *     ' + sMiddleRow)
        print(hBottomRow + '    *    ' + mBottomRow + '     *     ' + sBottomRow)
        print('Press Ctrl-C to quit.')
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital clock, by sinister geek')
    sys.exit()
