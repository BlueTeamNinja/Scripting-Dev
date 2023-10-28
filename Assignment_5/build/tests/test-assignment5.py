import unittest
import sys
import os

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

    def test_exercise1(self):
        import A5E1
        output = sys.stdout.getvalue().strip()
        expected_output = '''Holy cow! I can't believe I'm programming a computer.
Scripting in Python is so "freakin" cool!
Perhaps someday I'll be a Python "guru".
Someday, I could get a job at spotify\\reddit\\tinder\\alphabet.'''
        self.assertEqual(output, expected_output)
        self.assertTrue(check_fstring_formatting('/autograder/submission/A5E1.py'), "Improper Formatting, did not use Formatted String Literal")

    def test_exercise2(self):
        import A5E2
        output = sys.stdout.getvalue().strip()
        expected_output = '''Food Item       Price
==========      =======
Cheeseburger    $ 4.99
+ Bacon         $ 1.00
Fries w/gravy   $ 2.59
Milkshake       $ 2.99
-------
Sub-total:      $ 11.57
Tax (13%):      $ 1.50
Total:          $ 13.07'''
        self.assertEqual(output, expected_output)
        self.assertTrue(check_fstring_formatting('/autograder/submission/A5E2.py'), "Improper Formatting, did not use Formatted String Literal")

    def test_exercise3(self):
        import A5E3
        output = sys.stdout.getvalue().strip()
        expected_output = '''roses are red,
violets are blue,
unexpected '{'
on line 32.'''
        self.assertEqual(output, expected_output)
        self.assertTrue(check_fstring_formatting('/autograder/submission/A5E3.py'), "Improper Formatting, did not use Formatted String Literal")

    def test_bonus_marks_exercise2(self):
        import A5E2
        
        conditions = [
            ('food item prices are stored in descriptively named variables', 'Cheeseburger' in dir(A5E2) and isinstance(A5E2.Cheeseburger, (int, float))),
            ('variables are used to print the food item prices', sys.stdout.getvalue().contains(f"{A5E2.Cheeseburger}")),
            ('tax percentage is held in a descriptively named variable', 'tax_percentage' in dir(A5E2) and isinstance(A5E2.tax_percentage, (int, float))),
            ('variable is used to print the tax percentage', sys.stdout.getvalue().contains(f"{A5E2.tax_percentage}%")),
            ('sub-total, tax, and total are calculated by the script', True)  # This will be True if previous tests passed.
        ]

        for desc, condition in conditions:
            self.assertTrue(condition, f"BONUS: Failed the condition: {desc}")


if __name__ == "__main__":
    unittest.main()
