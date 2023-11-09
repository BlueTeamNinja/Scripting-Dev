
"""
This script takes a command line argument in inches and converts it to feet and inches.

Ex.
python A6E3.py 123

Output:
123" == 10'3"

Author: The Donkey from Shrek
"""

import sys

inches = sys.argv[1]

try:
    x = int(x)
    in_feet = int(x) // 12
    in_inches = int(x) - (12 * in_feet)
    print(f"{inches}\" == {in_feet}\'{in_inches}\"")
except:
    print(f"Error: Distance in inches must be an integer")