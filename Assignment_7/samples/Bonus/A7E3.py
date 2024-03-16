"""
Description: Calculates and prints total seconds from provided command line parameters.
Parameters: hours, minutes, seconds
Author: Your Name
"""

import sys
from datetime import datetime

# Constants
SEC_PER_MIN = 60
MIN_PER_HOUR = 60
HOURS_PER_DAY = 24

# Chosen start time
START_TIME = datetime(2024, 1, 9, 14, 0, 0)

def calc_total_seconds(hours=None, minutes=None, seconds=None):
    """ Calculate total seconds from hours, minutes, and seconds """
    if hours is None or minutes is None or seconds is None:
        now = datetime.now()
        delta = now - START_TIME
        total_seconds = delta.days * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN + delta.seconds
        return total_seconds

    try:
        return int(hours) * MIN_PER_HOUR * SEC_PER_MIN + int(minutes) * SEC_PER_MIN + int(seconds)
    except ValueError:
        return None

def main():
    if len(sys.argv) == 4:
        # If there are command line arguments, process them.
        hours, minutes, seconds = sys.argv[1:4]
        total_seconds = calc_total_seconds(hours, minutes, seconds)
        if total_seconds is not None:
            print(f"{hours} hr {minutes} min {seconds} sec == {total_seconds} sec")
        else:
            print("Invalid input. Please provide integer values for hours, minutes, and seconds.")
    else:
        # If no command line arguments, calculate from the chosen start date.
        total_seconds = calc_total_seconds()
        hours = total_seconds // SEC_PER_MIN // MIN_PER_HOUR
        minutes = (total_seconds // SEC_PER_MIN) % MIN_PER_HOUR
        seconds = total_seconds % SEC_PER_MIN
        print(f"{hours} hr {minutes} min {seconds} sec == {total_seconds} sec")

if __name__ == "__main__":
    main()
