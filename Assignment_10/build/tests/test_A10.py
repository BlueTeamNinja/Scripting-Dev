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
        self.assertEqual(A10E2.remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple', max=2), 2, "Tested remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple', max=2)")
        self.assertEqual(A10E2.remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple'), 1," Tested remove_str_from_list(['apple', 'banana', 'apple', 'pear'], 'apple')" )


    @weight(15)
    def test_remove_str_from_list_no_occurrences(self):
        """A10E2: Test remove_str_from_list function with no occurrences"""
        self.assertEqual(A10E2.remove_str_from_list(['banana', 'pear'], 'apple', 2), 0)

class TestA10E3(unittest.TestCase):

    @weight(0)
    def test_environment_sanity_check(self):
        """A10E3: Sanity Check"""
        try:
            with patch('builtins.input', side_effect=['50', 'no']*10), patch('random.randint', return_value=50):
                A10E3.main()
        except StopIteration:
            self.fail("Your script called 'input()' more times than expected.\nrandint was manually set to 50 in the environment\nInput was given the value 50,  then the word 'no' and it looped more than 10 times.\n\nPlease check your input handling and exit logic.\n Any following errors won't make sense or may crash as you have trapped the cyberpsyche in a timewarp continuum at the edge of the etherverse and the dreadnauts are coming.\nActually, you just have a loop that I can't figure out how to exit.  Correct guess, then no didn't work.")

    @weight(15)
    @patch('builtins.input', side_effect=['50', 'no'])
    def test_main_game_flow(self, mock_input):
        """A10E3: Test main function game flow"""
        try:
            with patch('random.randint', return_value=50):
                with patch('builtins.print') as mock_print:
                    A10E3.main()
                    mock_print.assert_called_with("Congratulations! You guessed it!")
        except StopIteration:
            self.fail("The function called 'input()' more times than expected. Test input:\n50 (which is the correct number)\nno\nPlease check your input handling logic, especially for invalid inputs.")

    @weight(15)
    def test_invalid_guess(self):
        """A10E3: Test handling of invalid guesses"""
        try:
            with patch('builtins.input', side_effect=['101', '50', 'no', 'yes', '50', 'no']), patch('random.randint', return_value=50):
                A10E3.main()

        except StopIteration:
            self.fail("The function called 'input()' more times than expected. Test input:\n101\n50 (which is the correct number)\nno\nyes\n50\nPlease check your input handling logic, especially for invalid inputs.")

if __name__ == '__main__':
    unittest.main()
