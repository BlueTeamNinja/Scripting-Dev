import unittest
import inspect
import sys
from gradescope_utils.autograder_utils.decorators import weight
import A7E1

sys.path.append('/autograder/submission')

class TestA7E1(unittest.TestCase):
    
    @weight(0)
    def test_global_input_usage(self):
        """A7E1: Check for python incantation"""
        source = inspect.getsource(A7E1)
        if ("__name__ == \"__main__\"" or "__name__ == '__main__'") not in source:
            self.fail("Warning: Python incantation not found")
        
        

    @weight(15)
    def test_fahrenheit_to_celsius(self):
        """A7E1: Testing convert_fahrenheit_to_celsius() with various values"""
        self.assertAlmostEqual(A7E1.convert_fahrenheit_to_celsius(32), 0.00, 2)
        self.assertAlmostEqual(A7E1.convert_fahrenheit_to_celsius(0), -17.78, 2)
        self.assertAlmostEqual(A7E1.convert_fahrenheit_to_celsius(-459.67), -273.15, 2)
    
    @weight(15)
    def test_fahrenheit_to_kelvin(self):
        """A7E1: Testing convert_celsius_to_fahrenheit() with various values"""
        self.assertAlmostEqual(A7E1.convert_fahrenheit_to_kelvin(32), 273.15, 2)
        self.assertAlmostEqual(A7E1.convert_fahrenheit_to_kelvin(0), 255.37, 2)
        self.assertAlmostEqual(A7E1.convert_fahrenheit_to_kelvin(-459.67), 0.00, 2)

if __name__ == '__main__':
    unittest.main()
