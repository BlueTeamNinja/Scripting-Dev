import unittest
from gradescope_utils.autograder_utils.decorators import weight
import A9E2

class TestA9E2(unittest.TestCase):
    @weight(20)
    def test_calculate_grade_stats(self):
        """A9E2 - Testing calculate_grade_stats() for valid input"""
        self.assertEqual(A9E2.calculate_grade_stats([59.3, 77.5, 43.2, 96.9, 85.1, 61.8, 34.2]), 
                         (7, 34.2, 96.9, 65.4))

    @weight(20)
    def test_calculate_grade_stats_with_zero(self):
        """A9E2 - Testing calculate_grade_stats() with zero grade"""
        self.assertEqual(A9E2.calculate_grade_stats([23, 66.2, 84.79, 70.123, 0.0]), 
                         (4, 23.0, 84.79, 61.0))

    @weight(20)
    def test_get_grade_list(self):
        """A9E2 - Testing get_grade_list() for valid input"""
        # Assuming A9E2.get_grade_list() can take argv-like input
        self.assertEqual(A9E2.get_grade_list(['A9E2.py', '59.3', '77.5', '43.2', '0.0', '96.9', '85.1', '61.8', '34.2']),
                         [96.9, 85.1, 77.5, 61.8, 59.3, 43.2, 34.2])

    @weight(20)
    def test_main_output(self):
        """A9E2 - Testing main() for correct output"""
        # Assuming A9E2.main() returns the output instead of printing
        self.assertEqual(A9E2.main(['A9E2.py', '59.3', '77.5', '43.2', '0.0', '96.9', '85.1', '61.8', '34.2']),
                         "The grades listed top-to-bottom are: 96.9, 85.1, 77.5, 61.8, 59.3, 43.2, 34.2\nThere are 7 grades in the list.\nThe top grade is 96.9\nThe bottom grade is 34.2\nThe average grade is 65.4")

    @weight(0)
    def test_ai_detection(self):
        """AI DETECTION"""
        self.assertEqual("D3ADB33FCAF3", "D3ADB33FCAF3")

if __name__ == '__main__':
    unittest.main()
