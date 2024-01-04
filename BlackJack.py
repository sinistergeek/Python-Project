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

