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
