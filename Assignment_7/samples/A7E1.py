# Module docstring
"""
This script converts temperature from Fahrenheit to Celsius and Kelvin.
It asks the user to input a temperature in Fahrenheit and prints out the equivalent in Celsius and Kelvin.
"""

# Functions
def convert_fahrenheit_to_celsius(fahrenheit):
    """ Convert Fahrenheit to Celsius """
    return (fahrenheit - 32) * 5.0/9.0

def convert_fahrenheit_to_kelvin(fahrenheit):
    """ Convert Fahrenheit to Kelvin """
    return convert_fahrenheit_to_celsius(fahrenheit) + 273.15

# Main script
if __name__ == "__main__":
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    kelvin = convert_fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit:.2f} F == {celsius:.2f} C == {kelvin:.2f} K")
