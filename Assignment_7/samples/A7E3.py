import sys

# Module docstring
"""
This script calculates total seconds from hours, minutes, and seconds passed as command line arguments.
"""

# Constants
SEC_PER_MIN = 60

# Functions
def calc_total_seconds(hours, minutes, seconds):
    """ Calculate total seconds from hours, minutes, and seconds """
    try:
        total_seconds = int(hours) * 3600 + int(minutes) * SEC_PER_MIN + int(seconds)
        return total_seconds
    except ValueError:
        return None

# Main script
if __name__ == "__main__":
    if len(sys.argv) == 4:
        hours, minutes, seconds = sys.argv[1:4]
        total_seconds = calc_total_seconds(hours, minutes, seconds)
        if total_seconds is not None:
            print(f"{hours} hr {minutes} min {seconds} sec == {total_seconds} sec")
        else:
            print("Invalid input. Please ensure all inputs are integers.")
    else:
        print("Please provide three integer values for hours, minutes, and seconds.")
