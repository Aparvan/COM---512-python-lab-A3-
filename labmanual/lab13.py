"""
Experiment 13: Arrange Words in Alphabetical Order Using a File
Question / Aim:

Write a Python program to read a text file. The program should print all the unique words from the file in alphabetical order.

Program:
"""
filename = input("Enter the file name: ")

with open(filename, "r") as file:
    text = file.read().lower()

words = text.split()

unique_words = sorted(set(words))

print("Unique words in alphabetical order:")

for word in unique_words:
    print(word)