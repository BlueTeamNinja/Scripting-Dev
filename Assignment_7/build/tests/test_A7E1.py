import unittest
from gradescope_utils.autograder_utils.decorators import weight
from A7E1 import convert_fahrenheit_to_celsius, convert_fahrenheit_to_kelvin

class TestA7E1(unittest.TestCase):
    
    @weight(5)
    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(32), 0.00, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(0), -17.78, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(-459.67), -273.15, 2)
    
    @weight(5)
    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convert_fahrenheit_to_kelvin(32), 273.15, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_kelvin(0), 255.37, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_kelvin(-459.67), 0.00, 2)

if __name__ == '__main__':
    unittest.main()
