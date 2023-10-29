import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
import sys
from importlib import import_module
import io

sys.path.append('/autograder/submission')
@weight(5)
def check_fstring_formatting(filename):
    """Testing for improper f-strings"""
    # Provide the same function definition as before...
    with open(filename, 'r') as f:
        content = f.read()
    improper_formatting = content.count('%') > 0 or ".format(" in content
    return not improper_formatting

class TestExercise2(unittest.TestCase):
    @weight(10)
    def test_exercise2(self):
        """Testing Exercise 3 - Proper Format output"""
        import A5E3
        output = sys.stdout.getvalue().strip()
        expected_poem = (
            "roses are red,\n"
            "violets are blue,\n"
            "unexpected '{'\n"
            "on line 32."
        )
        self.assertEqual(output, expected_poem.strip())

    @weight(10)
    def test_variables_used(self):
        """Testing Exercise 3 - Variables used"""
        import A5E3 as student_script
        self.assertTrue(hasattr(student_script, 'colour'), "The 'colour' variable is missing.")
        self.assertTrue(hasattr(student_script, 'flower'), "The 'flower' variable is missing.")
        self.assertTrue(hasattr(student_script, 'verb'), "The 'verb' variable is missing.")
        self.assertTrue(hasattr(student_script, 'line_num'), "The 'line_num' variable is missing.")
        self.assertEqual(student_script.colour, "red")
        self.assertEqual(student_script.flower, "violet")
        self.assertEqual(student_script.verb, "are")
        self.assertEqual(student_script.line_num, 32)

if __name__ == '__main__':
    unittest.main()
