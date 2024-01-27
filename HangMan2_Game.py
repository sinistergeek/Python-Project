import random,sys
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
                """,
r"""
 +--+
 |  |
 O  |
    |
    |
    |
                """,
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
                """,
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
                """,
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
                """,
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
                """,
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
                """
                ]
CATEGORY = 'Animals'
WORDS='ANT BABOON BADER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STROK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def main():
    print('Hangman, by sinistergeek')
    missedLetters = []
    correctLetters = []
    secretWord = random.choice(WORDS)
    while True:
        drawHangman(missedLetters, correctLetters, secretWord)
        guess = getPlayerGuess(missedLetters + correctLetters)
        if guess in secretWord:
            foundAllLetters = True
