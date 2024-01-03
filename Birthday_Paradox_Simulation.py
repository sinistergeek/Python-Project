import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birth = startOfYear + randomNumberOfDays
        brithdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayA == birthdayB:
            return BirthdayA


print('''Birthday Paradox, by AI Sweigart al@inventwithpython.com
      The Birday Paradox show us that in a group of N people,the odds
      that two of them have matching birthdays is suprisingly large.
      This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.
      (It's not acctually a paradox, it's  just a suprising result.)
      ''')
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()
print('Here are',numBDays,'birthdays:')
birthdays = getBirthdays(numBDays)
for i , birthday in enumerate(birthdays):
    if i !=0:
        print(',', end ='')
