import unittest
import re

# Helper function to check if variable names are in snake_case or camelCase
def check_variable_naming_convention(code):
    snake_case_pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
    camel_case_pattern = re.compile(r'^[a-z]+(?:[A-Z][a-z]+)*$')
    variables = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
    for var in variables:
        if snake_case_pattern.match(var) or camel_case_pattern.match(var):
            continue
        else:
            return False
    return True

class TestCommon(unittest.TestCase):

    @weight(10)
    def test_docstring_module(self):
        """Common - Module Docstring - 10 points"""
        self.assertIsNotNone(self.script.__doc__, "The module must have a docstring.")

    @weight(10)
    def test_variable_names(self):
        """Common - Sensible Variable Names - 10 points"""
        with open(self.script_file, 'r') as file:
            code = file.read()
            self.assertTrue(check_variable_naming_convention(code), "Variable names must follow snake_case or camelCase convention.")

    @weight(10)
    def test_file_naming(self):
        """Common - File Naming - 10 points"""
        self.assertTrue(hasattr(self, 'script_file'), "The script must have the appropriate file name.")

    @weight(10)
    def test_minimum_comments(self):
        """Common - Minimum Two Comments - 10 points"""
        with open(self.script_file, 'r') as file:
            code = file.read()
            comments = re.findall(r'#.*', code)
            self.assertGreaterEqual(len(comments), 2, "There should be at least two comments in the script.")
