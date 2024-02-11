import random,time,sys

print('''
        Rock , Paper, Scissors
      - Rock beats scissors.
      - Paper beats rocks.
      - Scissor beats paper.
      ''')
wins = 0
losses = 0
ties = 0
while True:
    while True:
        print('{} Wins, {} Losses, {} Tiles'.format(wins,losses,ties))

