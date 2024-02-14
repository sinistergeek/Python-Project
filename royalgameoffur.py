import random,sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

ALL_SPACEs = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghjklmnopstG'
O_TRACK = 'HabcdijklmnopqrG'

FLOWEr_SPACES = ('h','t','l','d','r')

BOARD_TEMPLATE = """
{}      {}
{} < {} < {} < {} |     |{} < {}
{} > {} > {} > {} > {} > {} > {} > {}
{} < {} < {} < {} < {} |  {} < {}
home    Goal
{}      {}
"""

def main():
    print('''
    The Royal Game of Ur,
    This is a 5,000 year old game. Two players must move their tokens from their home to their goal. On your turn you flip four coins and can move one token a number of spaces equal to the heads you got. Ur is a racing game; the first player to move all seven of their tokens to their goal wins. To do this, tokens must travel from their home to their goal
    ''')
