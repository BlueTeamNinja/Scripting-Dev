"""
This script prompts the user for a distance in inches and then prints the equivalent in feet and inches.

Example usage:
python A6E3.py

Author: Your Name
"""

# Constants
INCHES_PER_FEET = 12

def convert_inches_to_feet_and_inches(inches):
    feet = inches // INCHES_PER_FEET
    remaining_inches = inches % INCHES_PER_FEET
    return feet, remaining_inches

try:
    # Prompt user for input
    inches_input = input("Enter a distance in inches: ")
    
    # Convert input to an integer
    inches = int(inches_input)
    
    # Conversion
    feet, remaining_inches = convert_inches_to_feet_and_inches(inches)
    
    # Output the result
    print(f'{inches}" == {feet}\'{remaining_inches}"')
except ValueError:
    # Handle the exception if input is not an integer
    print("Error: Distance in inches must be an integer.")
