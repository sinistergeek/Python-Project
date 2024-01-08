import random
print(''' Carrot in a Box, by sinister geek
      This is a bluffing game for two human players. Each player has a box. One box has a carrot in it. To win, you have the box with carrot in it.
      This is a very simple and silly game.
      This first player looks into their box(the second player must close their eyes during this).The first player then says "There is a carrort in my box" or "There is not a carrot in my box". The second player then get to decide if they want to swap boxes or not.''')
input('Press Enter to begin....')
p1Name = input('Human player 1, Enter the name: ')
p2Name = input('Human player 2, Enter the name: ')
playersNames = p1Name[:11].center(11)+'     ' + p2Name[:11].center(11)
print('''
Here are TWO Boxes:
      -----------  -----------
      |         |   |       |
      |         |   |       |
      |         |   |       |
      |         |   |       |
      -----------  -----------
      ''')
print()
print(playerNames)
print(p1Name + ', you have a RED box in front of you. ')
print(p2Name + ', you have a GOLD in front of you.')
print()
print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!!!')
input('When ' + p2Name + 'has closed their eyes, press Enter...')
print()
print(p1Nmae + 'here is the inside of your box')
if random.randint(1,2) == 1:
    carrotInFirstBox = True

else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
    ---------- -----------
    |        | |         |
    | RED BOX| |GOLD BOX |
    |        | |         |
    ---------- -----------
    (carrot!)''')

else:
    print('''
    --------- --------
    |       | |      |
    |RED BOX| |GOLD  |
    |       | |BOX   |
    --------  --------
    (no carrot)''')
    print(playerNames)

