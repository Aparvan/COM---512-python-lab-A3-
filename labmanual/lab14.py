"""
Experiment 14: Create and Write Data into a Text File
Question / Aim:

Write a Python program to create a text file named MyFile.txt in write mode. The program should accept three lines of input from the user and write them into the file.

Program:
"""
file = open("MyFile.txt", "w")

line1 = input("Enter first line: ")
line2 = input("Enter second line: ")
line3 = input("Enter third line: ")

file.write(line1 + "\n")
file.write(line2 + "\n")
file.write(line3 + "\n")

file.close()

print("Data written successfully to MyFile.txt")