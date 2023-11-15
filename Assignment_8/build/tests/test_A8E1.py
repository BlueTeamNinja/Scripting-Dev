import unittest
import inspect
from gradescope_utils.autograder_utils.decorators import weight
from A8E1 import the_difference

class TestTheDifference(unittest.TestCase):

    @weight(2)
    def test_positive_numbers(self):
        """A8E1 - Positive Numbers Test - Checks if the function correctly handles positive integers"""
        self.assertEqual(the_difference(20, 10), 10, "Expected difference between 20 and 10 is 10")

    @weight(2)
    def test_negative_numbers(self):
        """A8E1 - Negative Numbers Test - Checks if the function correctly handles negative integers"""
        self.assertEqual(the_difference(-30, -20), 10, "Expected difference between -30 and -20 is 10")

    @weight(2)
    def test_mixed_numbers(self):
        """A8E1 - Mixed Numbers Test - Checks if the function correctly handles one positive and one negative integer"""
        self.assertEqual(the_difference(-10, 30), 40, "Expected difference between -10 and 30 is 40")

    @weight(2)
    def test_equal_numbers(self):
        """A8E1 - Equal Numbers Test - Checks if the function correctly returns 0 for equal integers"""
        self.assertEqual(the_difference(15, 15), 0, "Expected difference between 15 and 15 is 0")

    @weight(2)
    def test_non_integer_input(self):
        """A8E1 - Non-integer Input Test - Checks if the function correctly returns None for non-integer inputs"""
        self.assertIsNone(the_difference("hello", 10), "Expected output for non-integer input is None")

    @weight(10)
    def test_no_function_calls(self):
        """A8E1 - No Function Calls Test - Ensures no additional function calls like min(), max(), etc., are used"""
        source_code = inspect.getsource(the_difference)
        banned_functions = ['min', 'max', 'sum', 'sorted', 'any', 'all']
        for func in banned_functions:
            self.assertNotIn(func + '(', source_code, f"Function call to {func}() is not allowed")


if __name__ == '__main__':
    unittest.main()
