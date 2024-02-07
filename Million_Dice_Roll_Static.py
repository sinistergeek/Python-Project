import random,time
print('''Million Dice Roll Statistics Simulator
      Enter how amny six-sided dice you want to roll.''')
numberOfDice =int(input('> '))

results = {}
for i in range(numberOfDice,(numberOfDice * 6) + 1):
    results[i] = 0

print('Simulating 1,000,000 rolls of {} dice...'.format(numberOfDice))
lastPrintTime = time.time()
for i in range(10000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i/10000,1)))
        lastPrintTime = time.time()
    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1,6)
    results[total] = results[total] + 1


print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice,(numberOfDice * 6) + 1):
    roll = result[i]
    percentage = round(results[i]/ 10000,1)
    print('{} - {} rolls - {}%'.format(i,roll,percentage))
