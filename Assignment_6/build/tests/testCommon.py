import unittest
import os
import re
import ast
from gradescope_utils.autograder_utils.decorators import weight

class CommonTestSuite(unittest.TestCase):
    exercise_files = [
        '/autograder/submission/A6E1.py',
        '/autograder/submission/A6E2.py',
        '/autograder/submission/A6E3.py'
    ]

    def find_invalid_variables(self, tree):
        class VariableVisitor(ast.NodeVisitor):
            def __init__(self):
                self.invalid_vars = []

            def visit_Assign(self, node):
                # For simplicity, only consider single-target assignments
                if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                    var_name = node.targets[0].id
                    if not self.is_valid_variable_name(var_name):
                        self.invalid_vars.append(var_name)
                self.generic_visit(node)

            def is_valid_variable_name(self, name):
                # Variables should be longer than 6 characters to be checked
                if len(name) <= 6 or not name.islower():
                    return True
                snake_case_pattern = re.compile(r'^[a-z]+(_[a-z0-9]+)*$')
                camel_case_pattern = re.compile(r'^[a-z]+([A-Z][a-z0-9]+)*$')
                return bool(snake_case_pattern.match(name) or camel_case_pattern.match(name))

        visitor = VariableVisitor()
        visitor.visit(tree)
        return visitor.invalid_vars

    @weight(5)
    def test_variable_names(self):
        """Common - Very lazy check on your Variable Names"""
        all_invalid_vars = []
        for script_file in self.exercise_files:
            with open(script_file, 'r') as file:
                content = file.read()
                tree = ast.parse(content, filename=script_file)
                invalid_vars = self.find_invalid_variables(tree)
                if invalid_vars:
                    all_invalid_vars.extend(f"'{var}' in {script_file}" for var in invalid_vars)

        self.assertTrue(
            not all_invalid_vars,
            "Variables longer than 6 characters must follow snake_case or camelCase convention. "
            f"Invalid variable(s): {', '.join(all_invalid_vars)}"
        )

    @weight(5)
    def test_module_docstring(self):
        """Common - Module Docstring"""
        for script_file in self.exercise_files:
            with open(script_file, 'r') as file:
                code = file.read()
                self.assertTrue(code.startswith('"""'),
                                f"{script_file}: The module must start with a docstring.")

    @weight(5)
    def test_file_naming(self):
        """Common - File Naming"""
        for script_file in self.exercise_files:
            expected_file_name = os.path.basename(script_file)  # Extract filename from path
            self.assertTrue(os.path.exists(script_file),
                            f"{expected_file_name}: The script file {expected_file_name} must exist.")

    @weight(10)
    def test_minimum_comments(self):
        """Common - Minimum Two Comments"""
        for script_file in self.exercise_files:
            with open(script_file, 'r') as file:
                code = file.read()
                comments = re.findall(r'#.*', code)
                self.assertTrue(len(comments) >= 2,
                                f"{script_file}: There should be at least two comments in the script.")

if __name__ == "__main__":
    unittest.main()
