"""
verify_puzzlt_test.py

This module contains the unit tests for verify_puzzle.py
"""
import unittest
import verify_puzzle
from eight_puzzle import generate_new_puzzle
from puzzle_board import puzzle_board as pb

class TestEightPuzzle(unittest.TestCase):
    """Unit tests for eight puzzle game module"""

    def test_generate_puzzle(self):
        """Tests generating new puzzle on command"""
        puzzle_1 = generate_new_puzzle()
        puzzle_2 = generate_new_puzzle()

        self.assertNotEqual(puzzle_1.puzzle, puzzle_2.puzzle)


if __name__=="__main__":
    """Execute Script"""
    unittest.main()