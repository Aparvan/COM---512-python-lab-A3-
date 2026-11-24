"""
Experiment 12: Maximum of Three Numbers and Armstrong Number
Question / Aim:

Write a Python program to create a function max_of_three() that returns the largest of three numbers. Also create a function to check whether a given number is an Armstrong number or not.

Program:
"""
# Function to find maximum of three numbers

def max_of_three(a, b, c):
    return max(a, b, c)


# Function to check Armstrong number

def is_armstrong(n):
    temp = n
    power = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == n


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number:", max_of_three(a, b, c))

n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")