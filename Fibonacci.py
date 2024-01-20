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
