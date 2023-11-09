"""
This script converts a Fahrenheit temperature from a command-line argument to Celsius and Kelvin.

Example usage:
python A6E2.py 32

Author: Magical Unicorn
"""

from sys import argv

# Command-line argument to float
fahrenheit = float(argv[1])

# Perform conversions
celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15

# Print the temperatures, formatted to two decimal places
print(f"{fahrenheit:.2f} F == {celsius:.2f} C == {kelvin:.2f} K")

