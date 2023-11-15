import unittest
from gradescope_utils.autograder_utils.decorators import weight

from A7E1 import convert_fahrenheit_to_celsius, convert_fahrenheit_to_kelvin

class TestA7E1(unittest.TestCase):
    
    @weight(0)
    def test_global_input_usage(self):
        """Check for global input usage"""
        source = inspect.getsource(A7E1)
        if 'input(' in source and not 'input(' in source.split('def ')[1:]:
            print("You forgot to recite the incantation!  The rest of the errors won't make sense until you fix this.")
            self.fail("input() used at global level.")

    @weight(15)
    def test_fahrenheit_to_celsius(self):
        """A7E1: Testing convert_fahrenheit_to_celsius() with various values"""
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(32), 0.00, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(0), -17.78, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_celsius(-459.67), -273.15, 2)
    
    @weight(15)
    def test_fahrenheit_to_kelvin(self):
        """A7E1: Testing convert_celsius_to_fahrenheit() with various values"""
        self.assertAlmostEqual(convert_fahrenheit_to_kelvin(32), 273.15, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_kelvin(0), 255.37, 2)
        self.assertAlmostEqual(convert_fahrenheit_to_kelvin(-459.67), 0.00, 2)

if __name__ == '__main__':
    unittest.main()
