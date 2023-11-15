import unittest
import os
import ast
import importlib.util
from gradescope_utils.autograder_utils.decorators import weight

class TestCommon(unittest.TestCase):

    def setUp(self):
        """Setup common properties for the tests."""
        self.exercise_numbers = [1, 2, 3]
        self.submissions_path = "/autograder/submission/"

    @weight(10)
    def test_docstring_and_comments(self):
        """COMMON: Proper docstring and comments."""
        for n in self.exercise_numbers:
            file_path = os.path.join(self.submissions_path, f'A7E{n}.py')
            self.assertTrue(os.path.exists(file_path), f"File A7E{n}.py does not exist.")
            with open(file_path, 'r') as file:
                content = file.readlines()

                # Check for module docstring
                docstring = ast.get_docstring(ast.parse(''.join(content)))
                self.assertIsNotNone(docstring, f"A7E{n}.py must have a module docstring")
                self.assertIn('Description', docstring, f"A7E{n}.py docstring must contain 'Description'")
                self.assertIn('Parameters', docstring, f"A7E{n}.py docstring must contain 'Parameters'")
                self.assertIn('Author', docstring, f"A7E{n}.py docstring must contain 'Author'")

                # Check for at least two comments
                comments = [line for line in content if line.strip().startswith('#')]
                self.assertTrue(len(comments) >= 2, f"A7E{n}.py must contain at least 2 comments, please put them on their own line to be detected!")
        
    @weight(10)
    def test_main_function(self):
        """COMMON: Properly defined main function."""
        for n in self.exercise_numbers:
            file_path = os.path.join(self.submissions_path, f'A7E{n}.py')
            self.assertTrue(os.path.exists(file_path), f"File A7E{n}.py does not exist.")
            module_name = f'A7E{n}'
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Only exercise 1 and 3 require the main() function
            if n == 1 or n == 3: 

            # Check for the presence of a main function
                self.assertTrue(hasattr(module, 'main'), f"A7E{n}.py must have a main() function")

            # Check if '__name__ == "__main__"' block exists and calls main()
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    main_call = any("__name__ == \"__main__\":" in line for line in lines)
                    self.assertTrue(main_call, f"A7E{n}.py must call main() within the '__name__ == \"__main__\"' block")

    @weight(10)
    def test_file_naming(self):
        """COMMON: Script files are named correctly."""
        for n in self.exercise_numbers:
            file_path = os.path.join(self.submissions_path, f'A7E{n}.py')
            self.assertTrue(os.path.exists(file_path), f"File A7E{n}.py does not exist.")