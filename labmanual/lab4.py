"""
Experiment 4: Temperature Conversion
Question / Aim:

Write a Python program to convert temperature from Celsius to Fahrenheit and from Fahrenheit to Celsius using built-in functions.

"""
# Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius:", celsius)