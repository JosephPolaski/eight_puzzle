"""
verify_puzzlt_test.py

This module contains the unit tests for verify_puzzle.py
"""
import unittest
import verify_puzzle
from puzzle_board import puzzle_board as pb

class TestBuildTree(unittest.TestCase):
    """Unit test for building a tree of puzzle nodes"""

    def setUp(self):
        """Setup Class Attributes for multiple tests"""

        self._test_0 = pb()
        self._test_0.puzzle = [[1,2,3],[4, 5, None], [7, 8, 6]]   # assign test puzzle value, solvable in 1 move

        self._test_1 = pb()
        self._test_1.puzzle = [[1,2,3],[4, None, 5], [7, 8, 6]]   # assign test puzzle value, solvable in 2 moves

        self._test_2 = pb()
        self._test_2.puzzle = [[1,None,3],[4, 2, 5], [7, 8, 6]]   # assign test puzzle value, solvable in 3 moves

        self._test_4 = pb()
        self._test_4.puzzle = [[None,1,3],[4, 2, 5], [7, 8, 6]]   # assign test puzzle value, solvable in 4 moves

        self._test_5 = pb()
        self._test_5.puzzle = [[4,1,3],[None, 2, 5], [7, 8, 6]]   # assign test puzzle value, solvable in 5 moves

        self._test_6 = pb()
        self._test_6.puzzle = [[2,None,8],[5, 6, 4], [7, 3, 1]]   # assign test puzzle value, solvable in at least 23 moves (takes 15 mins)

        self._test_3 = pb() # creates a new random puzzle each time    

    def test_build_tree_fixed(self):
        """tests build tree method with fixed/controlled tests"""
        
        solution_set_0 = verify_puzzle.build_move_tree(self._test_0, 1)   # check if solvable with known puzzle and known number of moves
        self.assertTrue(solution_set_0[0], 'Test Puzzle 1 solvable')
      
        solution_set_1 = verify_puzzle.build_move_tree(self._test_1, 2)   # check if solvable with known puzzle and known number of moves
        self.assertTrue(solution_set_1[0], 'Test Puzzle 2 solvable')
      
        solution_set_2 = verify_puzzle.build_move_tree(self._test_2, 3)   # check if solvable with known puzzle and known number of moves
        self.assertTrue(solution_set_2[0], 'Test Puzzle 3 solvable')

     
        solution_set_3 = verify_puzzle.build_move_tree(self._test_4, 4)   # check if solvable with known puzzle and known number of moves
        self.assertTrue(solution_set_3[0], 'Test Puzzle 3 solvable')
        print(solution_set_3)
       
        solution_set_4 = verify_puzzle.build_move_tree(self._test_5, 5)   # check if solvable with known puzzle and known number of moves
        print(solution_set_4)
        self.assertTrue(solution_set_4[0], 'Test Puzzle 3 solvable')

        # this puzzle is solvable with this test but it takes 15 mins
        #print('-----------------------\nTesting Fixed Puzzle 5:\n-----------------------')
        #solution_set_5 = verify_puzzle.build_move_tree(self._test_6, 50)   # check if solvable with known puzzle and known number of moves
        #print(solution_set_5)
        #self.assertTrue(solution_set_5[0], 'Test Puzzle 3 solvable')

    
    def test_build_tree_random(self):
        """tests build tree method with fixed/controlled tests"""
        print('\nTesting Random Puzzle\n')
        solution_set = verify_puzzle.build_move_tree(self._test_3, 15)   # check if solvable with unknown puzzle and unknown amount of moves to win
        print(solution_set)
    
    def test_get_solving_moves(self):
        """tests generating of a solving move list"""

        solution_set_1 = verify_puzzle.build_move_tree(self._test_1, 5)   # check if solvable with known puzzle and known number of moves
        self.assertTrue(solution_set_1[0])

        solving_moves = verify_puzzle.get_solving_moves(solution_set_1[3])
        self.assertListEqual(solving_moves, ['right', 'down'])    

        solution_set_2 = verify_puzzle.build_move_tree(self._test_2, 5)   # check if solvable with known puzzle and known number of moves
        self.assertTrue(solution_set_1[0])

        solving_moves_2 = verify_puzzle.get_solving_moves(solution_set_2[3])
        self.assertListEqual(solving_moves_2, ['down','right', 'down'])    


if __name__=="__main__":
    """Execute Script"""
    unittest.main()