"""
This script converts a Fahrenheit temperature from a command-line argument to Celsius and Kelvin.

Example usage:
python A6E2.py 32

Author: Your Name
"""

import sys

# Check if temperature was provided
if len(sys.argv) < 2:
    print("Usage: python A6E2.py [temperature in Fahrenheit]")
    sys.exit(1)

# Convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

# Command-line argument to float
fahrenheit = float(sys.argv[1])

# Perform conversions
celsius = fahrenheit_to_celsius(fahrenheit)
kelvin = fahrenheit_to_kelvin(fahrenheit)

# Print the temperatures, formatted to two decimal places
print(f"{fahrenheit:.2f} F == {celsius:.2f} C == {kelvin:.2f} K")
