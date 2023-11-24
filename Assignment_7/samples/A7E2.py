# Module docstring
"""
This script defines a function to generate a command line string to run a given script.
"""

def script_run_command(file, directory='C:\\COMP86', interpreter='python'):
    """ Build a command line string to run a script """
    return f"{interpreter} '{directory}\\{file}'"
    
    
def main():
    command_line = script_run_command('script.py')
    print(command_line)

if __name__ == "__main__":
    main()