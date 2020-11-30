"""
puzzle_board.py 

This module contains all of the functions and methods to generate an 8 - puzzle in the form of a 2d list. 
"""

import random, copy

class puzzle_board:

    def __init__(self):
        self._puzzle = self.generate_puzzle()
        self._solved = [[1, 2, 3], [4, 5, 6], [7, 8, None]]    # represents solved state

    @property
    def puzzle(self):
        """puzzle preperty getter"""
        return self._puzzle

    @puzzle.setter
    def puzzle(self, value):
        """puzzle preperty setter"""
        self._puzzle = value

    @property
    def solved(self):
        """solved preperty getter"""
        return self._solved

    @solved.setter
    def solved(self, value):
        """solved preperty setter"""
        self._solved = value

    def get_blank_pos(self):
        """Get Blank Position"""

        # iterate through puzzle and return blank position
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):

                if self.puzzle[i][j] is None:
                    return [i, j]

    def find_valid_moves(self):

        valid_moves = []    # list of all possible moves
        lower_boundary = 0  # lower bound of puzzle grid
        upper_boundary = 2  # upper bound of puzzle grid   
        max_moves = 4

        blank_pos = self.get_blank_pos()    # fetch position of blank space

        # define what move directions are
        UP = [-1, 0]
        DOWN = [1,0]
        LEFT = [0,-1]
        RIGHT = [0, 1]       

        # UP
        if len(valid_moves) == 0 and (blank_pos[0] + UP[0]) >= lower_boundary: # check for valid UP move
            valid_moves.append('up')
        elif len(valid_moves) == 0 and (blank_pos[0] + UP[0]) < lower_boundary: # check for invalid UP move
            valid_moves.append(None)

        # DOWN
        if len(valid_moves) == 1 and (blank_pos[0] + DOWN[0]) <= upper_boundary: # check for valid DOWN move
            valid_moves.append('down')
        elif len(valid_moves) == 1 and (blank_pos[0] + DOWN[0]) > upper_boundary: # check for invalid DOWN move
            valid_moves.append(None)

        # LEFT
        if len(valid_moves) == 2 and (blank_pos[1] + LEFT[1]) >= lower_boundary: # check for valid LEFT move
            valid_moves.append('left')
        elif len(valid_moves) == 2 and (blank_pos[1] + LEFT[1]) < lower_boundary: # check for invalid LEFT move
            valid_moves.append(None)
        
        # RIGHT
        if len(valid_moves) == 3 and (blank_pos[1] + RIGHT[1]) <= upper_boundary: # check for valid RIGHT move
            valid_moves.append('right')
        elif len(valid_moves) == 3 and (blank_pos[1] + RIGHT[1]) > upper_boundary: # check for invalid RIGHT move
            valid_moves.append(None)
        
        return valid_moves
    
    def make_move(self, direction):
        """
        Swaps number from the specified direction with the blank 
        space.

        :param direction: direction values can be 'up', 'down', 'left', 'right'
        :return updated_state = updates puzzle to the new state
        """
        blank_space = self.get_blank_pos()  # get postion of blank tile
        possible_moves = self.find_valid_moves()    # get valid moves list

        # get positions of all surrounding peices
        up_pos = [(blank_space[0]-1), blank_space[1]]
        down_pos = [(blank_space[0]+1), blank_space[1]]
        left_pos = [blank_space[0], (blank_space[1]-1)]
        right_pos = [blank_space[0], (blank_space[1]+1)]
        new_pos = None

        # check if desired move is valid
        if direction not in possible_moves:
            return False
        
        # Move is valid proceed with position Swap
        if direction == 'up':
            new_pos = up_pos
        elif direction == 'down':
            new_pos = down_pos
        elif direction == 'left':
            new_pos = left_pos
        elif direction == 'right':
            new_pos = right_pos

        # move if a valid move has been given
        if new_pos is not None:
            swap = self.puzzle[blank_space[0]][ blank_space[1]]  # grab blank space 
            self.puzzle[blank_space[0]][ blank_space[1]] = self.puzzle[new_pos[0]][ new_pos[1]]
            self.puzzle[new_pos[0]][ new_pos[1]] = swap
            return True


    def generate_puzzle(self):
        """Generates a Randomized 8-puzzle board with 1 blank space (None value)"""

        already_used = [] # keeps track of already used numbers

        puzzle_board = []   # represents the puzzle board

        for i in range(0, 3):
            row = []    # create row
            
            while len(row) < 3:

                rand_num = random.randint(1, 9) # generate random integer between 1 - 8           

                if rand_num not in already_used:
                    if rand_num == 9:
                        row.append(None)    # 9 represents blank space
                    else:
                        row.append(rand_num)    # add number to row

                    already_used.append(rand_num)   # add to number to already_used
            
            puzzle_board.append(row)  # add row to board
        
        return puzzle_board   

    def is_solvable(self):
        """
        Checks if the puzzle is even solvable. Based on number of inversions
        an 8 puzzle is not solvable if it has an odd number of inversions.
        This is because horizontal movements result in no change to number of inversions,
        but each verticle move results in a change of plus or minus 2 to the number of inversions
        in a puzzle. Therefore if a puzzle is generated with an odd number of inversions, it is 
        unsolvable.
        """

        puzzle_1D = []
        inversions = 0

        # convert puzzle to 1 dimensional grid ignoring the blank space
        for i in range(0, len(self.puzzle)):
            for j in range(0, len(self.puzzle[i])):
                if self.puzzle[i][j] is not None:
                    puzzle_1D.append(self.puzzle[i][j])
        
        # convert puzzle to 1 dimensional grid ignoring the blank space
        for i in range(0, len(puzzle_1D)):
            for j in range(i + 1, len(puzzle_1D)):
                if puzzle_1D[j] < puzzle_1D[i] :
                    inversions += 1        

        # Check for even number of inversions
        if inversions % 2 == 0:
            return True # Solvable
        else:
            return False # Unsolvable

if __name__=="__main__":
    """Execute Script"""
    test = puzzle_board()  
    print(test.puzzle)
    
    test.is_solvable()
    
   