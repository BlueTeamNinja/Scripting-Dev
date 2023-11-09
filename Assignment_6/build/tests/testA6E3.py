import unittest
import sys
from gradescope_utils.autograder_utils.decorators import weight
from unittest.mock import patch
from io import StringIO
import importlib

# Adjust the path if necessary to correctly import the student's submission
sys.path.append('/autograder/submission')

class TestExercise3(unittest.TestCase):

    @weight(15)
    def test_exercise3_handling_of_input(self):
        """Testing Exercise 3 - Correct Handling of Input"""
        with patch('builtins.input', return_value='123'), patch('sys.stdout', new_callable=StringIO) as stdout:
            try:
                # Attempt to import the student's script within the context of the patched input
                # The module name must match the filename of the student's Python script
                student_module = importlib.import_module('A6E3')
                importlib.reload(student_module)
            except IndexError:
                self.fail('Why are you looking for arguments? Check the instructions again. The rest of the errors on this assignment may not make sense because of this.')
            except Exception as e:
                self.fail(f'An error occurred: {str(e)}')

            # Check the output format
            output = stdout.getvalue().strip()
            expected_output = '123" == 10\'3"'
            self.assertEqual(output, expected_output, "The output format does not match the expected result for integer input.")

    @weight(20)
    def test_exercise3_integer_input(self):
        """Testing Exercise 3 - Correct Output for Integer Input"""
        with patch('builtins.input', return_value='123'), patch('sys.stdout', new_callable=StringIO) as stdout:
            student_module = importlib.import_module('A6E3')
            importlib.reload(student_module)
            output = stdout.getvalue().strip()
            expected_output = '123" == 10\'3"'
            self.assertEqual(output, expected_output, "The output format does not match the expected result for integer input.")

    @weight(20)
    def test_exercise3_non_integer_input(self):
        """Testing Exercise 3 - Correct Handling of Non-Integer Input"""
        with patch('builtins.input', return_value='paneer'), patch('sys.stdout', new_callable=StringIO) as stdout:
            try:
                student_module = importlib.import_module('A6E3')
                importlib.reload(student_module)
            except SystemExit:
                pass  # We expect a SystemExit if the student's code handles errors via sys.exit()
            output = stdout.getvalue().strip()
            expected_output = "Error: Distance in inches must be an integer."
            self.assertEqual(output, expected_output, "The script did not properly handle non-integer input.")
 
    @weight(10)
    def test_constant_exists(self):
        """Testing Exercise 3 - Constant Exists"""
        student_module = importlib.import_module('A6E3')
        self.assertTrue(hasattr(student_module, 'INCHES_PER_FEET'), "The constant 'INCHES_PER_FEET' is missing. Are you trying to use a magic number?")

    @weight(5)
    def test_constant_value(self):
        """Testing Exercise 3 - Constant Value"""
        student_module = importlib.import_module('A6E3')
        self.assertEqual(getattr(student_module, 'INCHES_PER_FEET', None), 12, "The constant 'INCHES_PER_FEET' does not have the value of 12.")

if __name__ == '__main__':
    unittest.main()
