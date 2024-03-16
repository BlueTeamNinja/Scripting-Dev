import unittest
import os
import importlib.util
from datetime import datetime
from gradescope_utils.autograder_utils.decorators import weight
from unittest.mock import patch
from io import StringIO

class TestBonus(unittest.TestCase):

    submissions_path = "/autograder/submission/"

    def setUp(self):
        self.exercise_numbers = [1, 2, 3]
        self.start_times = [
            datetime(2024, 1, 9, 14, 0, 0)  # January 9th, 2024 @ 1400
        ]

    def load_module(self, exercise_number):
        file_path = os.path.join(self.submissions_path, f'A7E{exercise_number}.py')
        module_name = f'A7E{exercise_number}'
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    @weight(10)
    def test_exercise_1_bonus(self):
        """BONUS: Test Exercise 1 for error-checking."""
        module = self.load_module(1)
        with patch('builtins.input', side_effect=['not_a_number']), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            module.main()
            output = mock_stdout.getvalue().strip()
            expected_error_msg = "That ain't gonna fly."
            self.assertIn(expected_error_msg, output, "Exercise 1 failed: Non-numeric input did not produce the expected error message.")

    @weight(20)
    def test_exercise_2_bonus(self):
        """BONUS: Test for get_script_name() and get_script_location() in Exercise 2."""
        from A7E2 import get_script_name, get_script_location
        actual_name = get_script_name()
        expected_name = 'A7E2.py'
        self.assertEqual(actual_name, expected_name, f"Expected {expected_name}, got {actual_name}")

        actual_location = get_script_location()
        expected_location = '/autograder/source'
        self.assertEqual(actual_location, expected_location, f"Expected {expected_location}, got {actual_location}")

    @weight(30)
    def test_exercise_3_bonus(self):
        """BONUS: Test Exercise 3 for default parameters."""
        module = self.load_module(3)
        current_datetime = datetime.now()
        # Adjusted to handle one or more start times
        possible_seconds = [int((current_datetime - start_time).total_seconds()) for start_time in self.start_times]
        actual_seconds = module.calc_total_seconds()
        leeway_seconds = 10 * 60  # 10 minutes leeway in seconds
        # Check if actual_seconds is within leeway_seconds of any possible_seconds
        passed = any(abs(actual_seconds - possible) <= leeway_seconds for possible in possible_seconds)
        self.assertTrue(passed, f"Exercise 3 failed: Expecting one of the values within ±600 seconds (10 minutes) of {possible_seconds}\nReceived: {actual_seconds}.")

if __name__ == '__main__':
    unittest.main()
