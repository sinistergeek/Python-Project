import copy
import sys

TOTAL_DISKS = 5

COMPLETE_TOWER = list(range(TOTAL_DISKS,0,-1))

def main():
    print("The Tower of Hanoi")
    towers = {'A':copy.copy(COMPLETE_TOWER),'B':[],'C':[]}
    while True:
        displayTowers(towers)
        fromTower, toTower = askForPlayerMove(towers)
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)
        if COMPLETE_TOWER in (towers['B'],towers['C']):
            displayTowers(towers)
            print('You have solved the puzzle! Well done!')
            sys.exit()


def askForPlayerMove(towers):
    while True:
        print('Enter the letters of "from" and "to" towers, or QUIT.')
