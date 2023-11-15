import unittest
import os
import ast
import importlib.util
from gradescope_utils.autograder_utils.decorators import weight

class TestCommon(unittest.TestCase):

    def setUp(self):
        """Setup common properties for the tests."""
        self.exercise_numbers = [1, 2]
        self.submissions_path = "/autograder/submission/"

    @weight(10)
    def test_docstring_and_comments(self):
        """COMMON: Proper docstring and comments."""
        for n in self.exercise_numbers:
            file_path = os.path.join(self.submissions_path, f'A8E{n}.py')
            self.assertTrue(os.path.exists(file_path), f"File A8E{n}.py does not exist.")
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Check for module docstring
                docstring = ast.get_docstring(ast.parse(''.join(content)))
                self.assertIsNotNone(docstring, f"A8E{n}.py must have a module docstring")
                self.assertIn('Description', docstring, f"A8E{n}.py docstring must contain 'Description'")
                self.assertIn('Parameters', docstring, f"A8E{n}.py docstring must contain 'Parameters'")
                self.assertIn('Author', docstring, f"A8E{n}.py docstring must contain 'Author'")

                # Check for at least two comments
                comments = [line for line in content if line.strip().startswith('#')]
                self.assertTrue(len(comments) >= 2, f"A8E{n}.py must contain at least 2 comments, please put them on their own line to be detected!")

    @weight(30)
    def test_global_namespace_usage(self):
        """COMMON: No code in the global namespace other than allowed function definitions or Python incantation."""
        for n in self.exercise_numbers:
            file_path = os.path.join(self.submissions_path, f'A8E{n}.py')
            self.assertTrue(os.path.exists(file_path), f"File A8E{n}.py does not exist.")
            with open(file_path, 'r') as file:
                content = file.read()
                tree = ast.parse(content)

                for node in ast.iter_child_nodes(tree):
                    if isinstance(node, ast.FunctionDef):
                        continue  # Skip function definitions

                    if isinstance(node, (ast.Assign, ast.Expr)):
                        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                            continue  # Skip docstrings

                        line_number = node.lineno
                        line_content = content.splitlines()[line_number-1].strip()
                        self.fail(f"A8E{n}.py has code in the global namespace: '{line_content}' on line {line_number}")


    @weight(10)
    def test_file_naming(self):
        """COMMON: Script files are named correctly."""
        for n in self.exercise_numbers:
            file_path = os.path.join(self.submissions_path, f'A8E{n}.py')
            self.assertTrue(os.path.exists(file_path), f"File A8E{n}.py does not exist.")