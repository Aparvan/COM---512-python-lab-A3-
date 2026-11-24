"""
Experiment 1: Demonstrate Various Data Types and Built-in Functions
Question / Aim:

Write a Python program to demonstrate various data types and the use of built-in functions such as abs(), len(), min(), round() and isalnum().
"""
# Type checking of various data types

a = 10
b = 3.14
c = "Hello"

print("Type(10):", type(a))
print("Type(3.14):", type(b))
print("Type('Hello'):", type(c))

# Demonstrating built-in functions

# abs() function
num = -5
print("abs(-5):", abs(num))

# len() function
text = "Hello, World!"
print("len('Hello, World!'):", len(text))

# min() function
numbers = [5, 2, 8, 1, 9]
print("min([5, 2, 8, 1, 9]):", min(numbers))

# round() function
decimal = 3.14159
print("round(3.14159):", round(decimal))

# isalnum() function
s1 = "Hello123"
s2 = "Hello 123"

print("isalnum('Hello123'):", s1.isalnum())
print("isalnum('Hello 123'):", s2.isalnum())