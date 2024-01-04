import random, sys
HEARTS = chr(9829)
DIAMONds = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''
    Blackjack, by sinister geek
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 throught 10 are worth their face value.
        (H)it to take another card
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing. 
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
    ''')
    money = 5000
    while True:
        if money <= 0 :
            print("Your're broke!")
            print("Good thing weren't playing wiuth real monmey.")
            print('Thanks for playing!')
            sys.exit()

        print('Money:',money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(),deck.pop()]
        playerHand = [deck.pop(),deck.pop()]
        print('Bet:',bet)
        while True:
            displayHands(playerHand,dealerHand,False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)
            if move == 'D':
                additionalBet = getBet(min(bet,(money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:',bet)


            if move in ('H','D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ('S','D'):
                break
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)
                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue.....')
                print('\n\n')
        displayHands(playerHand,dealerHand,True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You losts!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie,the bet is returned to you.')
        input('Press Enter to continue....')
        print('\n\n')

def getBet(maxBet):
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDuck():
    deck = []
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit))
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck
