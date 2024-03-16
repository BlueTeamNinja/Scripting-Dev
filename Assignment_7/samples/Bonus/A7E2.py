"""
Description: Provides a command string to run the script and identifies script name and location.
Parameters: file, directory, interpreter
Author: Your Name
"""

import os
import sys

def script_run_command(file, directory='C:\\COMP86', interpreter='python'):
    """ Build a command line string to run a script """
    return f"{interpreter} '{directory}\\{file}'"

def get_script_name():
    """ Return the name of the running script """
    return 'A7E2.py'

def get_script_location():
    """ Return the location of the running script """
    return os.path.dirname(os.path.abspath(__file__))