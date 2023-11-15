# Module docstring
"""
This script defines a function to generate a command line string to run a given script.
"""

def script_run_command(file, directory='C:\\COMP86', interpreter='python'):
    """ Build a command line string to run a script """
    print(f"{interpreter} '{directory}\\{file}'")
    return