
"""
Description:
This script uses the function convert_fahrenheit_to_celcius() to take an integer and 
converts it into kelvin and celcius and prints that out to the user

Parameters:(fahrenheit)

Author: Keelin Collins
"""
 
#temp coversions for F-C held in function
def convert_fahrenheit_to_celsius(fahrenheit):
     output=(fahrenheit-32)/1.8
     return output
    
#temp conversion for F-K held in function
def convert_fahrenheit_to_kelvin(fahrenheit):
    output= (fahrenheit-32)/1.8+273.15 
    return output
    
#error checking if a float is not entered as the input     
def main():
    try:
        user_input=float(input("Enter a tempature in Fahrenheit:"))
        CELSIUS=convert_fahrenheit_to_celsius(user_input)
        KELVIN=convert_fahrenheit_to_kelvin(user_input)
        print(f'{user_input:.2f}F == {CELSIUS:.2f}C == {KELVIN:.2f}K')
    except:
        print(f"That ain't gonna fly.")
#main statement
if __name__ =='__main__':  
    main()     