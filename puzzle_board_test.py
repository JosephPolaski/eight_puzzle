"""
puzzle_board_test.py

This module contains the unit tests for puzzle_board_test.py
"""
import unittest
from .puzzle_board import puzzle_board as pb

class TestPuzzleBoard(unittest.TestCase):
    """Unit test for Puzzle Board Class"""

    def setUp(self):
        """Setup Class Attributes for multiple tests"""

        self._test_1 = pb()
        self._test_1.puzzle = [[1,2,3],[4, None, 5], [7, 8, 6]]   # assign test puzzle value, solvable in 2 moves

        self._test_2 = pb()
        self._test_2.puzzle = [[4,1,3],[None, 2, 5], [7, 8, 6]]   # assign test puzzle value, solvable in 5 moves

        self._test_3 = pb()
        self._test_3.puzzle = [[2,1,3],[4, None, 6], [7, 5, 8]]   # assign test puzzle value, unsolvable

    def test_get_valid_moves(self):
        """Test if getting valid moves works"""

        children = self._test_1.find_valid_moves()
        self.assertListEqual(children, ['up', 'down', 'left', 'right'])

    def test_is_solvable(self):
        """Tests the general solvability verifying function"""

        result = self._test_2.is_solvable()
        self.assertTrue(result)

if __name__=="__main__":
    """Execute Script"""
    unittest.main()