"""
Experiment 3: String Operations
Question / Aim:

Write a Python program to perform various string operations. Count the number of alphabets in a given string, extract characters within a given range, and check whether the string is alphanumeric or not.

Program:

"""
string = "Welcome to Python Programming"

# Counting the number of alphabets

count = 0

for char in string:
    if char.isalpha():
        count += 1

print("Number of alphabets in string:", count)

# Extracting characters in the given range

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

extracted_chars = string[start_index:end_index]

print("Extracted characters:", extracted_chars)

# Checking if the string is alphanumeric

print("Is the string alphanumeric?", string.isalnum())