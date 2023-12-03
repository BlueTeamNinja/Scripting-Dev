import unittest
import importlib
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight

# Import the modules for testing
import A10E1
import A10E2
import A10E3

class TestA10E1(unittest.TestCase):
    
    @weight(5)
    def test_all_divisible(self):
        """A10E1: Test all_divisible function"""
        self.assertTrue(A10E1.all_divisible([9, 12, 6, 15], 3), "Tested several numbers divisible by 3, expecting True")
        self.assertFalse(A10E1.all_divisible([9, 11, 6, 15], 3), "Tested several numbers not all divisible by 3, expecting False")

    @weight(5)
    def test_any_divisible(self):
        """A10E1: Test any_divisible function"""
        self.assertTrue(A10E1.any_divisible([20, 12, 24, 8], 4), "Tested several numbers divisible by 4, expecting True")
        self.assertFalse(A10E1.any_divisible([9, 11, 13, 27], 4), "Tested no numbers divisible by 4, expecting False")

    @weight(10)
    def test_difference(self):
        """A10E1: Test difference function"""
        self.assertEqual(A10E1.difference([9, 12, 6, 8]), -11)
        self.assertEqual(A10E1.difference([10, 5, 1, 3]), 1)

class TestA10E2(unittest.TestCase):

    @weight(15)
    def test_remove_str_from_list(self):
        """A10E2: Test remove_str_from_list function"""
        self.assertEqual(A10E2.remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple', 2), 2)
        self.assertEqual(A10E2.remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple'), 1)

    @weight(15)
    def test_remove_str_from_list_no_occurrences(self):
        """A10E2: Test remove_str_from_list function with no occurrences"""
        self.assertEqual(A10E2.remove_str_from_list(['banana', 'pear'], 'apple', 2), 0)

class TestA10E3(unittest.TestCase):

    @weight(15)
    @patch('builtins.input', side_effect=['50', 'no'])
    def test_main_game_flow(self, mock_input):
        """A10E3: Test main function game flow"""
        with patch('random.randint', return_value=50):
            with patch('builtins.print') as mock_print:
                A10E3.main()
                mock_print.assert_called_with("Congratulations! You guessed it!")

    @weight(15)
    def test_invalid_guess(self):
        """A10E3: Test handling of invalid guesses"""
        with patch('builtins.input', side_effect=['101', '50', 'no']), patch('random.randint', return_value=50):
            with patch('builtins.print') as mock_print:
                A10E3.main()
                mock_print.assert_any_call("Invalid guess. Please enter a number between 1 and 100.")

if __name__ == '__main__':
    unittest.main()
