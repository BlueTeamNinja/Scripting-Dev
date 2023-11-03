"""
This script accepts a name as a command-line argument and prints out a personalized message.

Example usage:
python A6E1.py Jeremy

Author: Your Name
"""

import sys

# Ensure there is a command-line argument provided
if len(sys.argv) < 2:
    print("Usage: python A6E1.py [name]")
    sys.exit(1)

# The name is taken from the first command-line parameter
name = sys.argv[1]

# Generate and print the personalized messages
print(f"{name} is the most amazing person I have ever met.")
print(f'My mother is always saying, "You need to be more like {name}."')
print(f"Dear {name}: You rock!")
