"""
Experiment 7: Student Records Using Dictionary
Question / Aim:

Write a Python program to create records of students. Store each student's roll number, name, branch and marks in a dictionary and search for a student using roll number.

Program:
"""
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    students[roll] = {
        "name": name,
        "branch": branch,
        "marks": marks
    }

roll = input("Enter roll number to search: ")

if roll in students:
    print(students[roll])
else:
    print("Student not found")