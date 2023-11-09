import unittest
from gradescope_utils.autograder_utils.decorators import weight
from A7E3 import calc_total_seconds

class TestA7E3(unittest.TestCase):
    
    @weight(20)
    def test_calc_total_seconds_valid(self):
        self.assertEqual(calc_total_seconds(1, 2, 3), 3723)
        self.assertEqual(calc_total_seconds(23, 60, 59), 86459)
    
    @weight(10)
    def test_calc_total_seconds_invalid(self):
        self.assertIsNone(calc_total_seconds(23, 60, 'samosa'))
        self.assertIsNone(calc_total_seconds(1, 'poutine', 3))

if __name__ == '__main__':
    unittest.main()
