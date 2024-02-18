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
