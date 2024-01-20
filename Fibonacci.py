import sys
print('''
Fibonacci Sequence, by sinistergeek The fibnacci sequence begins with 0 and 1, and the next number is the sum of the previous two numbers. THe sequence continues forever:0,1,1,2,3,5,13,21...
      ''')
while True:
    while True:
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        print('Please enter a number greater than 0, or QUIT.')
    print()
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth==2:
        print('0,1')
        print()
        print('The #2 Fibbonacci number is 1.')
        continue
    if nth >= 10000:
        print('WARNING: THis will take a while to display on the ')
        print('screen. If you want to quit this program before it is')
        print('done,press Ctrl-C.')
        input('Press Enter to begin....')

    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated =2
    print('0,1,',end='')

    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1
        print(nextNumber, end='')
        if fibNumberrsCalculated == nth:
            print()
            print()
            print('The #',fibNumbersCalculated,'Fibonacci','number is ',nextNumber, sep='')
            break
        print(',',end='')
        secondToLastNumber = lastNumber
        lastNumber = nextNumber

