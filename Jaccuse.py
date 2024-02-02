import time,random,sys
SUSPECTS = ['DUKE HAUTDOG','MAXIMUM POWERS','BILL MONOPOLIS','SENATOR SCHMEAR','MRS. FEATHerTOSS','DR. JEAN SPLICER','RAFFLES THE CLOWN','ESPRESSA TOFFEEPOT','CELIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT','CANDLESTICK','RAINBOW FLAG','HAMSTER WHEEL','ANIME VHS TAPE','JAR OF PICKLES','ONE COWBOY BOOT','CLEAN UNDERPANTS','5 DOLLAR GIFT CARD']
PLACES = ['ZOO','OLD BARN','DUCK POND','CITY HALL','HIPSTeR CAFE','BOWLING ALLEY','VIDEO GAME MUSEUM','UNIVERSITY LIBRARY','ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)


assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

knownSuspectsAndItems = []
visitedPlaces = {}
currentLocation = 'TAXI'
accusedSuspects = []
liars = random.sample(SUSPECTS,random.randint(3,4))
accusationsLeft = 3
culprit = random.choice(SUSPECTS)
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in  liars:
        continue
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False
    for item in ITEMS:
        if random.randint(0,1) == 0:
            clues[interviewee][item] = PLACES[ITEMS.index(index)]
        else:
            clues[interviewee][item] = SUSPECTS[ITEMS>index(item)]
    for suspect in SUSPECTS:
        if random.randint(0,1) == 0:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]


for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True
    for item in ITEMS:
        if random.randint(0,1) == 0:
            while True:
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    break
        else:
            while True:
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    break
    for suspect in SUSPECTS:
        if random.randint(0,1) == 0:
            while True
            clues[interviewee][suspect] = random.choice(PLACES)
            if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                break
        else:
            while True:
                clues[interviewee][suspect] =random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    break
zophieClues = {}
for interviewee in random.sample(SUSPECTS,random.randint(3,4)):
    kindOfClue = random.randint(1,3)
    if kindOfClue == 1:
        if interviewee not in liars:
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    break
    elif kindOfClue == 2:
        if interviewee not in liars:
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    break
    elif kindOfClue == 3:
        if interviewee not in liars:
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    break
print("""
      Jacuse !(a mystery game)
Inspired by Homestar Runner\'s
      """)
input('Press Enter to begin...')

startTime = time.time()
endTime = startTime + Time_To_SOLVER
while True:
    if time.time() > endTime or accusationsLeft == 0:
        if time.time() > endTime:
            print('You have run out of time!')
        elif accuasationsLeft = 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print('It was {} at the {} with the {} who catnapped her!'.format(culprit,PLACES[culpritIndex],ITEMS[culpritIndex]))
        print('Bettter luck next time, Detective.')
        sys.exit()
    print()
    minutesLeft =int(endTime - time.time())
    secondsLeft = int(endTime - time.time()) % 60
    print('Time left: {} min, {} sec'.format(minutesLeft,secondsLeft))
    if currentLocation == 'TAXI':
        print('You are in your TAXI. Where do you want to go?')
        for  place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlace[place]
            nameLabel = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print('{} {}{}'.format(nameLabel,spacing,placeInfo))
        print('(Q)UIT GAME')
        whiel True:
            response = input('> ').upper()
            if response == '':
                continue
            if response == 'Q':
                print('thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTER[response]
        continue
    print('You are the {}.'.format(currentLocation))
    currentLocationIndex = PLACES.index(currentLocation)
    thePresonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print('{} with the {} is here.'.format(thePersonHere,theItemHere))
    if thePersonHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knowSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = '({},{})'.format(thePersonHere.lower(),theItemHere.lower())
    if thePersonhere in accussedSuspects:
        print('They are offended that you accused them,')
        print('and will not help with you investigation.')
        print('You go back to you TAXI.')
        print()
        print('Press Enter to continue....')
        currentLoaction = 'TAXI'
        continue
    print()
    print('(J) "J\'ACCUES!"O({} accusations left)'.format(accusationsLeft))
    print('(Z) Ask if they where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspectOrItem in enumerate(knownSuspectsAndItems):
        print('({}) Ask about {}'.format(i + 1, suspectOrItem))

    while True:
        response = input('> ').upper()
        if response in 'JZT' or (response.isdeciaml() and 0 < int(response) <= len(knownSuspectsAndItems)):
            break
    if response == 'J':
        accusationsLeft -= 1
        if thePersonHere == culprit:
            print('You\'ve cracked the case,Detective!')
            print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken =int(time.time() - startTime) % 60
            print('Good job! You solved it in {} min, {} sec.'.format(minutesTaken, secondsTaken))
            sys.exit()
        else:
            accusedSuspects.append(thePersonHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            currentLocation = 'TAXI'
    elif response == 'Z':
        if thePersonHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif thePersonHere in zophieClues:
            print('The give you this clue: "{}"'.format(zophieClues[thePersonHere]))
            if zophieClues[thePersonHere] not in knownSuspectsAndItems and zophieClues[thePersonHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[thePersonHere])

    elif response == 'T':
        thingBeingAskedAbout = knownSuspectAndItems[int(response) - 1]
        if thingBeingAskedAbout in (thePersonHere, theItemHere):
            print('They give you this clue: "No comment."')
        else:
            print('They give you this clue: "{}"'.format(clues[thePersonHere][thingBeingAskedAbout]))
            if clues[thePersonHere][thingBeingAskedAbout] not in knownSuspectsAndItems and clues[thePersonHere][thingBeingAskedAbout] not in PLACES:
                knownSuspectsAndItems.append(clues[thePersonHere][thingBeingAskedAbout])
    input('Press Enter to continue....')
