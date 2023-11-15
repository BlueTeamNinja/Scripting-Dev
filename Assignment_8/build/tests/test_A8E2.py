import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight
from A8E2 import get_player_choice, get_computer_choice, game_result

class TestRockPaperScissors(unittest.TestCase):

    @weight(5)
    def test_valid_input(self):
        """A8E2 - Valid Input Test - Checks if the function handles valid inputs correctly"""
        with patch('builtins.input', return_value='R'):
            self.assertEqual(get_player_choice(), "ROCK", "Expected player choice for 'R' is 'ROCK'")

    @weight(5)
    def test_invalid_input(self):
        """A8E2 - Invalid Input Test - Checks if the function handles invalid inputs correctly"""
        with patch('builtins.input', return_value='X'):
            self.assertEqual(get_player_choice(), "X", "Expected player choice for 'X' is 'X'")

    @weight(15)
    def test_game_result(self):
        """A8E2 - Game Result Test - Checks if the game result is calculated correctly"""
        self.assertEqual(game_result("ROCK", "SCISSORS"), 1, "Expected result for ROCK vs SCISSORS is win (1)")
        self.assertEqual(game_result("PAPER", "ROCK"), 1, "Expected result for PAPER vs ROCK is win (1)")
        self.assertEqual(game_result("SCISSORS", "PAPER"), 1, "Expected result for SCISSORS vs PAPER is win (1)")
        self.assertEqual(game_result("ROCK", "PAPER"), -1, "Expected result for ROCK vs PAPER is lose (-1)")
        self.assertEqual(game_result("PAPER", "SCISSORS"), -1, "Expected result for PAPER vs SCISSORS is lose (-1)")
        self.assertEqual(game_result("SCISSORS", "ROCK"), -1, "Expected result for SCISSORS vs ROCK is lose (-1)")
        self.assertEqual(game_result("ROCK", "ROCK"), 0, "Expected result for ROCK vs ROCK is draw (0)")

    @weight(5)
    def test_computer_choice(self):
        """A8E2 - Computer Choice Test - Checks if the computer's choice is randomly generated"""
        # Mocking random.choice to return a specific value
        with patch('random.choice', return_value='rock'):
            self.assertEqual(get_computer_choice().upper(), "ROCK", "Expected computer choice is 'ROCK'")

if __name__ == '__main__':
    unittest.main()
