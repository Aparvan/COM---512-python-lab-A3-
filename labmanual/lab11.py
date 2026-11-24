"""
Experiment 11: Right-Angled Triangle and Area Using Heron's Formula
Question / Aim:

Write a Python program that accepts the lengths of three sides of a triangle as input. The program should indicate whether the triangle is a right-angled triangle or not. Also find the area of the triangle using Heron's formula.

Program:
"""
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

sides = sorted([a, b, c])

if a + b > c and a + c > b and b + c > a:

    if round(sides[0]**2 + sides[1]**2, 2) == round(sides[2]**2, 2):
        print("Right Angled Triangle")
    else:
        print("Not a Right Angled Triangle")

    s = (a + b + c) / 2

    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

    print("Area of Triangle:", area)

else:
    print("Invalid Triangle")