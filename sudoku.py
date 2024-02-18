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
    
