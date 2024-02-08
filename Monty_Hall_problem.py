import random,sys

ALL_CLOSED = """
+  + +  + +  +
 1    2    3
"""

FIRST_GOAT = """
+  + +  + +  +
 go    2    3
"""

SECOND_GOAT = """
+  + +  + +  +
  1   go    3
"""

THIRD_GOAT = """
+  + +  + +  +
  1    2   go
"""

FIRST_CAR_OTHERS_GOAT = """
+  + +  + +  +
 car  go   go
"""

SECOND_CAR_OTHERS_GOAT = """
+  + +  + +  +
 go   car   go
"""
THIRD_CAR_OTHERS_GOAT = """
+  + +  + +  +
go    go   car
"""

print('''
      The Monty Hall Problem, you can pick one of three doors. One door has a new car for a prize. The other two doors have worthless goats: {} 
      Say you pick Door #1.
      Before the door you choose is opened,another door with a goat is opened: {} You can choose to eitehr open the door you originally picked or swap to the other unopened door.
      It may seem like it doesn't matter if you swap or not, but your odds do improve if you swap doors! THis program demonstrates the Monty Hall Problem by letter you do repated experiments.
'''.format(ALL_CLOSED,THIRD_GOAT))
input('Press Enter to start....')

swapWins = 0
swapLosses = 0
stayWins = 0
stayLosses = 0
while True:
    doorThatHasCar = random.randint(1,3)
    print(ALL_CLOSED)
    while True:
        print('Pick a door 1,2, or 3 (or "quit" to stop):')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response == '1' or response == '2' or response == '3':
            break
    doorPick = int(response)
    while True:
        showGoatDoor = random.randint(1,3)
        if showGoatDoor != doorPick and showGoatDoor != doorThatHasCar:
            break
    if showGoatDoor == 1:
        print(FIRST_GOAT)
    elif showGoatDoor == 2:
        print(SECOND_GOAT)

    elif showGoatDoor == 3:
        print(THIRD_GOAT)
    print('Door {} contains a goat!'.format(showGoatDoor))
    while True:
        print('Do you want to swap doors? Y/N')
        swap = input('> ').upper()
        if swap == 'Y' or swap == 'N':
            break
    if swap == 'Y':
        if doorPick == 1 and showGoatDoor  == 2:
            doorPick = 3
        elif doorPick == 1 and showGoatDoor == 3:
            doorPick = 2

