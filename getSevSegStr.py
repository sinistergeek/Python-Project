def getSevSegStr(number, minWidth=0):
    number = str(number).zfill(minWidth)
    rows = ['','','']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
