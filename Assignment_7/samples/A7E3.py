import sys

# Module docstring
"""
This script calculates total seconds from hours, minutes, and seconds passed as command line arguments.
"""

# Constants
SEC_PER_MIN = 60

# Main Body
def main():
    """ Main Body of Script """
    # Get command line arguments
    hours = sys.argv[1]
    minutes = sys.argv[2]
    seconds = sys.argv[3]
    
    # Calculate total seconds
    total_seconds = calc_total_seconds(hours, minutes, seconds)
    
    # Print results
    if total_seconds is None:
        print("Please enter valid numbers for hours, minutes, and seconds.")
    else:
        print(f"{hours}:{minutes}:{seconds} == {total_seconds} seconds")

# Functions
def calc_total_seconds(hours, minutes, seconds):
    """ Calculate total seconds from hours, minutes, and seconds """
    try:
        total_seconds = int(hours) * 3600 + int(minutes) * SEC_PER_MIN + int(seconds)
        return total_seconds
    except:
        return None

# Main script
if __name__ == "__main__":
    main()
