import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, partial_credit
import sys
import importlib
import io

sys.path.append('/autograder/submission')

class TestExercise2Bonus(unittest.TestCase): 
    @weight(0)
    def test_exercise2_bonus(self):
        """Testing Exercise 2 Bonus - Proper use of variables and calculations"""
        # Dynamically import and reload A5E2 to ensure it runs
        import A5E2
        importlib.reload(A5E2)
        output = sys.stdout.getvalue().strip()
        expected_vars = ['cheeseburger', 'fries_w_gravy', 'bacon', 'milkshake', 'tax']
        for var in expected_vars:
            assert var in dir(A5E2), f"Variable {var} not found!"

        # Validate that calculations in the output are correct
        expected_subtotal = A5E2.cheeseburger + A5E2.fries_w_gravy + A5E2.bacon + A5E2.milkshake
        expected_tax = expected_subtotal * A5E2.tax
        expected_total = expected_subtotal + expected_tax

        # Using f-strings to construct the expected output based on the variables' values
        expected_output = f'''Food Item\tPrice
==========\t=======
Cheeseburger\t$ {A5E2.cheeseburger:.2f}
+ Bacon\t\t$ {A5E2.bacon:.2f}
Fries w/gravy\t$ {A5E2.fries_w_gravy:.2f}
Milkshake\t$ {A5E2.milkshake:.2f}
-------
Sub-total:\t$ {expected_subtotal:.2f}
Tax ({A5E2.tax*100:.0f}%):\t$ {expected_tax:.2f}
Total:\t\t$ {expected_total:.2f}'''

        self.assertEqual(output, expected_output)

        # Award bonus marks if everything passed
        set_score(20)


if __name__ == "__main__":
    unittest.main()
