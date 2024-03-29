import copy, random, sys

EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH

class SudokuGrid:
    def __init__(self, originalSetup):
        self.originalSetup = originalSetup
        self.grid = {}
        self.resetGrid()
        self.moves = []

    def resetGrid(self):
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1,GRID_LENGTH + 1):
                self.grid[(x,y)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0
        y = 0
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x,y)] = self.originalSetup[i]
                i += 1
            y += 1

    def makeMove(self,column,row,number):
        x = 'ABCDEFGHI'.find(column)
        y = int(row) - 1
        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False
        self.grid[(x,y)] = number
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        if self.moves == []:
            return
        self.moves.pop()
        if self.moves == []:
            self.resetGrid()
        else:
            self.grid = copy.copy(self.moves[-1])
    
    def display(self):
        print(' ABC DEF GHI')
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    print(str(y + 1) + ' ',end='')
                print(self.grid[(x,y)] + ' ',end='')
                if x == 2 or x == 5:
                    print('| ',end='')
            print()
            if y == 2 or y == 5:
                print('=======+-----+---')
    def _isCompleteSetOfNumbers(self,numbers):
        return sorted(numbers) == list('123456789')

    def isSolved(self):
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x,row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number =self.grid[(column,y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False
        for boxx in (0,3,6):
            for boxy in (0,3,6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x,boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False
        return True
print('Sudoku Puzzle')
input('Press Enter to begin...')
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()

for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

while True:
    grid.display()
    if grid.isSolved():
        print('Congratulations! You solved the puzzle')
        print('Thanks for playing!')
        sys.exit()

    while True:
        print()
        print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
        print('(For example, a move looks like "B4 9".)')
        action = input('> ').upper().strip()
        if len(action) > 0 and action[0] in ('R','N','U','O','Q'):
            break
        if len(action.split()) == 2:
            space,number =action.split()
            if len(space) != 2:
                continue
            column, row = space
            if column not in list('ABCDEFGHI'):
                print('There is no column',column)
                continue
            if not row.isdecimal() or not (1 <= int(row) <=9):
                print('There is no row',row)
                continue
            if not (1 <= int(number) <= 9):
                print('Select a number from 1 to 9, not ',number)
                continue
            break
    print()
    if action.startswith('R'):
        grid.resetGrid()
        continue
    if action.startswith('N'):
        grid = SudokuGrid(random.choice(puzzles))
        continue
    if action.startswith('U'):
        grid.undo()
        continue
    if action.startswith('O'):
        originalGrid = SudokuGrid(grid.originalSetup)
        print('The original grid looked like this:')
        originalGrid.display()
        input('Press Enter to continue.....')

    if action.startwith('Q'):
        print('Thanks for playing!')
        sys.exit()

    if grid.makeMove(column,row,number) == False:
        print('You cannot overwrite the original grid\'s numbers.')
        print('Enter ORIGINAL to view the original gird.')
        input('Press Enter to continue....')
