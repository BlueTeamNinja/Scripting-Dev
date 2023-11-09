import unittest
import sys
import os
from gradescope_utils.autograder_utils.decorators import weight
from unittest.mock import patch
from io import StringIO


class TestExercise2(unittest.TestCase):
    script_file = '/autograder/submission/A6E2.py'
    @weight(30)
    def test_exercise2(self):
        """Testing Exercise 2 - Correct Output and Formatting"""
        with patch('sys.argv', ['A6E2.py', '-50']), patch('sys.stdout', new_callable=StringIO) as stdout:
            import A6E2
            output = stdout.getvalue().strip()
            expected_output = '-50.00 F == -45.56 C == 227.59 K'
            self.assertEqual(output, expected_output, "The output format does not match the expected result using '-50'.")
            self.assertTrue(check_fstring_formatting('/autograder/submission/A6E2.py'), "Improper Formatting, did not use Formatted String Literal")

def check_fstring_formatting(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if 'print(' in line:
            if '%' in line or '.format(' in line:
                return False
            if 'f"' not in line and "f'" not in line:
                return False
    return True
