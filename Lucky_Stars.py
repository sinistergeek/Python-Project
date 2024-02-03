import random

GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["+------+"]
SKULL_FACE = ["+-----+"]
QUESTION_FACE = ["+----+"]

FACE_WIDTH = 13
FACE_HEIGHT = 7

print("
A "press your luck" game where you roll dice with Stars,Skulls and Question Marks.
      On your turn, you pull three random dice from the dice cup and roll them. You can roll Start, Skills and Question Marks. You can end your turn and get one point per Star. If you choose to roll again, you keep the Question Marks and pull new dice to replace the Stars and Skulls. If you collect there Skulls, you lose all your Stars and end your turn. When a plaer get 13 points, everyone else gets more turn before the game ends. Whoever has the most points wins. There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup. Gold dice have more Stars, Bronze dice have more Skulls, and Silver is even.
      ")
print('How many players are there?')
while True:
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
