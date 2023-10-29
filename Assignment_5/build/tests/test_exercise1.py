import unittest
import sys
import os
from gradescope_utils.autograder_utils.decorators import weight


sys.path.append('/autograder/submission')
def check_fstring_formatting(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if 'print(' in line:
            if '%' in line or '.format(' in line:
                return False
    return True

class TestAssignment5(unittest.TestCase):
    @weight(10)
    def test_exercise1(self):
        """Testing Exercise 1 - Its all or nothing"""
        import A5E1
        output = sys.stdout.getvalue().strip()
        expected_output = '''Holy cow! I can't believe I'm programming a computer.
Scripting in Python is so "freakin" cool!
Perhaps someday I'll be a Python "guru".
Someday, I could get a job at spotify\\reddit\\tinder\\alphabet.'''
        self.assertEqual(output, expected_output)
        self.assertTrue(check_fstring_formatting('/autograder/submission/A5E1.py'), "Improper Formatting, did not use Formatted String Literal")

if __name__ == "__main__":
    unittest.main()
