import random
print('''
Powerball Lotter, by sinistergeek
      Each powerball lottery ticket costs $2. The jackpot for this game is $1.586 billion! It doesn't matter what the jackpot is,through, because the odds are 1 in 292,201,338, so you won't win. This simulation gives you the thrill of playing without wasting money.
      ''')
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number.(For example: 5 17 23 42 50)')
    response = input('> ')
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, separated by spaces.')
        continue
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27,35, or 62.')
        continue

    for i in range(5):
        if not(1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue
    break

while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')

    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15 or 22.')
        continue
