# Module docstring
"""
This script defines a function to generate a command line string to run a given script.
"""

# Function
def script_run_command(file, directory='C:\\COMP86', interpreter='python'):
    """ Generate a command line string to run a script """
    return f"{interpreter} '{directory}\\{file}'"

# Test the function (not required by the assignment, but for demonstration)
if __name__ == "__main__":
    print(script_run_command('A7E2.py', 'D:\\COMP 86\\Assignment 7'))
