def getSevSegStr(number, minWidth=0):
    number = str(number).zfill(minWidth)
    rows = ['','','']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
        elif numeral == '-':
            rows[0] += '    '
            rows[1] += '____'
            rows[2] += '    '
        elif numeral == '0':
            rows[0] += '    '
            rows[1] += '   0 '
            rows[2] += '  o  '

        elif numeral == '1':
            rows[0] += '    '
            rows[1] += '1   '
            rows[2] += '1   '
        elif numeral == '2':
            rows[0] += '    '
            rows[1] += '2   '
            rows[2] += '2   '
        elif numeral == '3':
            rows[0] += '    '
            rows[1] += '3   '
            rows[2] += '3   '
        elif numeral == '4':
            rows[0] += '    '
            rows[1] += '4   '
            rows[2] += '4   '
        elif numeral == '5':
            rows[0] += '    '
            rows[1] += '5   '
            rows[2] += '5   '

        elif numeral == '6':
            rows[0] += '    '
            rows[1] += '6   '
            rows[2] += '6   '

        elif numeral == '7':
            rows[0] += '    '
            rows[1] += '7   '
            rows[2] += '7   '

        elif numeral == '8':
            rows[0] += '    '
            rows[1] += '8   '
            rows[2] += '8   '

        elif numeral == '9':
            rows[0] += '    '
            rows[1] += '9   '
            rows[2] += '9   '

        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)

if __name__ == '__main__':
    print('')
