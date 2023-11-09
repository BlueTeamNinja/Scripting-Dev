import unittest
import sys
import os
from gradescope_utils.autograder_utils.decorators import weight
from unittest.mock import patch
from io import StringIO

class TestExercise1(unittest.TestCase):
    script_file = '/autograder/submission/A6E1.py'
    @weight(30)
    def test_exercise1(self):
        """Testing Exercise 1 - Correct Output and Format"""
        with patch('sys.argv', ['A6E1.py', 'Jeremy']), patch('sys.stdout', new_callable=StringIO) as stdout:
            import A6E1
            output = stdout.getvalue().strip()
            expected_output = '''Jeremy is the most amazing person I have ever met.
My mother is always saying, "You need to be more like Jeremy."
Dear Jeremy: You rock!'''
            self.assertEqual(output, expected_output, "The output format does not match the expected result.")
