import unittest
from gradescope_utils.autograder_utils.decorators import weight

import sys
import io
from contextlib import redirect_stdout
import importlib
import A9E2


class TestA9E2(unittest.TestCase):
    @weight(10)
    def test_calculate_grade_stats(self):
        """A9E2 - Testing calculate_grade_stats() for valid output"""
        self.assertEqual(A9E2.calculate_grade_stats([59.3, 77.5, 43.2, 96.9, 85.1, 61.8, 34.2]), 
                         (7, 34.2, 96.9, 65.42857142857143))

    @weight(20)
    def test_calculate_grade_stats_with_zero(self):
        """A9E2 - Testing calculate_grade_stats() with zero grade"""
        self.assertEqual(A9E2.calculate_grade_stats([23, 66.2, 84.79, 70.123, 0.0]), 
                         (4, 23.0, 84.79, 61.02825))

    @weight(20)
    def test_get_grade_list(self):
        """A9E2 - Testing get_grade_list() for processing input from command line"""
        original_argv = sys.argv
        try:
            test_args = ['A9E2.py', '59.3', '77.5', '43.2', '96.9', '85.1', '61.8', '34.2']
            sys.argv = test_args
            importlib.reload(A9E2)

            expected_result = [96.9, 85.1, 77.5, 61.8, 59.3, 43.2, 34.2]
            self.assertEqual(A9E2.get_grade_list(), expected_result)
#           self.fail("Your script isn't handling command-line arguments.  If you are still making this mistake at this point you need to do some reading and catch up.")

        finally:
            sys.argv = original_argv

    @weight(20)
    def test_get_grade_list(self):
        """A9E2 - Testing get_grade_list() with a zero grade"""
        original_argv = sys.argv
        try:
            test_args = ['A9E2.py', '59.3', '77.5', '43.2', '96.9', '0.0','85.1', '61.8', '34.2']
            sys.argv = test_args
            importlib.reload(A9E2)

            expected_result = [96.9, 85.1, 77.5, 61.8, 59.3, 43.2, 34.2]
            self.assertEqual(A9E2.get_grade_list(), expected_result)
        finally:
            sys.argv = original_argv

    @weight(50)
    def test_main_output(self):
        """A9E2 - Testing main() for complete functionality"""
        original_argv = sys.argv
        try:
            test_args = ['A9E2.py', '59.3', '77.5', '43.2', '0.0', '96.9', '85.1', '61.8', '34.2']
            sys.argv = test_args

            importlib.reload(A9E2)


            # Redirect stdout to capture the print output from main
            with io.StringIO() as buf, redirect_stdout(buf):
                A9E2.main()
                output = buf.getvalue()

            expected_output = (
                "The grades listed top-to-bottom are: 96.9, 85.1, 77.5, 61.8, 59.3, 43.2, 34.2\n"
                "There are 7 grades in the list.\n"
                "The top grade is 96.9\n"
                "The bottom grade is 34.2\n"
                "The average grade is 65.4\n"
            )

            self.assertEqual(output, expected_output)
        finally:
            sys.argv = original_argv

    @weight(0)
    def test_ai_detection(self):
        """AI DETECTION"""
        self.assertEqual("D3ADB33FCAF3","D3ADB33FCAF3")

if __name__ == '__main__':
    unittest.main()
