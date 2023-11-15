"""
Description: Converts temperature from Fahrenheit to Celsius and Kelvin, with input error handling.
Parameters: None
Author: Abe - The Divine
"""

def convert_fahrenheit_to_celsius(fahrenheit):
    """ Convert Fahrenheit to Celsius """
    return (fahrenheit - 32) * 5.0 / 9.0

def convert_fahrenheit_to_kelvin(fahrenheit):
    """ Convert Fahrenheit to Kelvin """
    return convert_fahrenheit_to_celsius(fahrenheit) + 273.15

def get_temperature_input():
    """ Prompt user for temperature in Fahrenheit and validate input. """
    try:
        return float(input("Enter a temperature in Fahrenheit: "))
    except ValueError:
        print("That ain't gonna fly, Marty.")
        return None

def main():
    fahrenheit = get_temperature_input()
    if fahrenheit is not None:
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        kelvin = convert_fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit:.2f} F == {celsius:.2f} C == {kelvin:.2f} K")

if __name__ == "__main__":
    main()
