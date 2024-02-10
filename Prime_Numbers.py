import math, sys

def main():
    print('''
    Prime Numbers 
    It is the numbers that are only evenly divisible by one and themselves. They are used in a variety of practical applications but can't be predicted. They must be calculated one at a time.''')
    print()

    while True:
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 100000000000 (n zero) or another number.')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break

    input('Press Ctrl-C at any time to quit. Press Enter to begin.....')
    while True:
        if isPrime(num):
            print(str(num) + ', ', end='',flush=True)
        num = num + 1

def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2,int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
