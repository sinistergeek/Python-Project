import random, sys
print('''
    Dice Roller, by sinister geeek
    Enter what kind and how many dice to roll. The format is the number of dice, followed by "d",followed by the number of sides the dice have. You can also add a plus or minus adjustment.
    Examples:
    3d6 rolls three 6-sided  dice
    1d10+2 rolls one 10-sided die, and adds 2
    2d38-1 rolls two 380sided die, and subracts 1
    QUIT quits the program
      ''')
while True:
    try:
        diceStr = input('>  ')
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
