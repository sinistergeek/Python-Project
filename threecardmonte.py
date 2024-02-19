import random,time
NUM_SWAPS = 16
DELAY = 0.8
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
LEFT = 0
MIDDLE = 1
RIGHT = 2

def displayCards(cards):
    row = ['','','','','']
    for i,card in enumerate(cards):
        rank,suit =card
        rows[0] += '      '
        rows[1] += '|{}  |'.format(rank.ljust(2))
        rows[2] += '| {} |'.format(suit)
        rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    for i in range(5):
        print(rows[i])

def getRandomCard():
    while True:
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS,DIAMONDS,SPADES,CLUBS])
        if rank != 'Q' and suit != HEARTS:
            return (rank,suit)


print('Three-Card Monte')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how the cards move.')
print()
cards = [('Q',HEARTS),getRandomCard(),getRandomCard()]
random.shuffle(cards)
print('Here are the cards:')
displayCards(cards)
input('Press Enter when you are ready to begin....')
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m','m-r','l-r','m-l','r-m','r-l'])
    if swap == 'l-m':
        print('swapping left and middle....')
        cards[LEFT],cards[MIDDLE] = cards[MIDDLE],cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE],cards[RIGHT] = cards[RIGHT],cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT],cards[RIGHT] = cards[RIGHT],cards[MIDDLE]
    elif swap == 'm-l':
        print('swapping middle and left..')
        cards[MIDDLE],cards[LEFT] = cards[LEFT],cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT],cards[MIDDLE] = cards[MIDDLE],cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left')
        cards[RIGHT],cards[LEFT] = cards[LEFT],cards[RIGHT]
    time.sleep(DElAY)

print('\n'* 60)

while True:
    print('Which card has the Queen of HEARTS?(LEFT MIDDLE RIGHT)')
    guess = input('> ').upper()
    if guess in ['LEFT','MIDDLE','RIGHT']:
        if guess == 'LEFT':
            guessIndex = 0
        elif guess == 'MIDDLE':
            guessIndex = 1
        elif guess == 'RIGHT':
            guessIndex = 2
        break

