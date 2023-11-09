import unittest
import os
import ast
import importlib.util
from gradescope_utils.autograder_utils.decorators import weight

class TestCommon(unittest.TestCase):

    def setUp(self):
        self.exercise_numbers = [1, 2, 3]
        self.submissions_path = "/autograder/submissions/"

    @weight(10)
    def test_docstring_and_comments(self):
        """Test if scripts contain proper docstring and comments."""
        for n in self.exercise_numbers:
            with self.subTest(i=n):
                file_path = os.path.join(self.submissions_path, f'A7E{n}.py')
                with open(file_path, 'r') as file:
                    content = file.read()
                    parsed_content = ast.parse(content)

                    # Check for module docstring
                    self.assertIsNotNone(ast.get_docstring(parsed_content), f"A7E{n}.py must have a module docstring")

                    # Check for 'Description', 'Parameters', 'Author' in docstring
                    docstring = ast.get_docstring(parsed_content)
                    self.assertIn('Description', docstring, f"A7E{n}.py docstring must contain 'Description'")
                    self.assertIn('Parameters', docstring, f"A7E{n}.py docstring must contain 'Parameters'")
                    self.assertIn('Author', docstring, f"A7E{n}.py docstring must contain 'Author'")

                    # Check for at least two comments
                    comments = [node.value for node in ast.walk(parsed_content) if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str)]
                    self.assertTrue(len(comments) >= 2, f"A7E{n}.py must contain at least 2 comments")

    @weight(10)
    def test_main_function(self):
        """Test if scripts contain a properly defined main function."""
        for n in self.exercise_numbers:
            with self.subTest(i=n):
                file_path = os.path.join(self.submissions_path, f'A7E{n}.py')
                module_name = f'A7E{n}'
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Check for the presence of a main function
                self.assertTrue(hasattr(module, 'main'), f"A7E{n}.py must have a main() function")

                # Check if '__name__ == "__main__"' block exists and calls main()
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    main_call = any("__name__ == \"__main__\":" in line for line in lines)
                    self.assertTrue(main_call, f"A7E{n}.py must call main() within the '__name__ == \"__main__\"' block")

    @weight(10)
    def test_file_naming(self):
        """Test if script files are named correctly."""
        for n in self.exercise_numbers:
            with self.subTest(i=n):
                self.assertTrue(os.path.isfile(os.path.join(self.submissions_path, f'A7E{n}.py')), f"File A7E{n}.py does not exist in the submissions path")

# The following is not necessary when using JSONTestRunner in Gradescope
# as it uses the discovery mechanism to run tests.
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
