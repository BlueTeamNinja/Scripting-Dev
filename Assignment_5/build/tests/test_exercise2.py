import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
import sys
from importlib import import_module
import io

sys.path.append('/autograder/submission')
@weight(5)
def check_fstring_formatting(filename):
    """Testing for improper f-strings"""
    # Provide the same function definition as before...
    with open(filename, 'r') as f:
        content = f.read()
    improper_formatting = ".format(" in content
    return not improper_formatting

class TestExercise2(unittest.TestCase):
    @weight(20)
    def test_exercise2(self):
        """Testing Exercise 2 - Proper Format output"""
        import A5E2
        output = sys.stdout.getvalue().strip()
        expected_output = '''Food Item\tPrice
==========\t=======
Cheeseburger\t$ 4.99
+ Bacon\t\t$ 1.00
Fries w/gravy\t$ 2.59
Milkshake\t$ 2.99
-------
Sub-total:\t$ 11.57
Tax (13%):\t$ 1.50
Total:\t\t$ 13.07'''
        
        self.assertEqual(output, expected_output.strip())
        self.assertTrue
        (check_fstring_formatting('/autograder/submission/A5E2.py'), "Improper Formatting, did not use Formatted String Literal")
    


if __name__ == "__main__":
    unittest.main()
