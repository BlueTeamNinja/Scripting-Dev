import unittest
from gradescope_utils.autograder_utils.decorators import weight
import sys

from A7E2 import script_run_command

sys.path.append('/autograder/source')

class TestA7E2(unittest.TestCase):
    
    @weight(30)
    def test_script_run_command(self):
        """A7E2: Checking script_run_command() with various inputs"""
        self.assertEqual(script_run_command('script.py'), "python 'C:\\COMP86\\script.py'")
        self.assertEqual(script_run_command('A2E2.ps1', 'C:\\Homework', 'pwsh'), "pwsh 'C:\\Homework\\A2E2.ps1'")
        self.assertEqual(script_run_command('script.ps1', interpreter='pwsh'), "pwsh 'C:\\COMP86\\script.ps1'")
        self.assertEqual(script_run_command('A7E2.py', 'D:\\COMP 86\\Assignment 7'), "python 'D:\\COMP 86\\Assignment 7\\A7E2.py'")
        self.assertEqual(script_run_command('M7A3.py', interpreter='python3', directory='.'), "python3 '.\\M7A3.py'")

if __name__ == '__main__':
    unittest.main()
