"""
Experiment 8: Student Database Using List of Tuples
Question / Aim:

Write a Python program to create a student database using a list of tuples. Each record should contain roll number, name, branch and CGPA. Search for a student using roll number.

Program:

"""
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    students.append((roll, name, branch, cgpa))

print("\nStudent Records:")

for s in students:
    print(s)

roll = input("\nEnter roll number to search: ")

found = False

for s in students:
    if s[0] == roll:
        print("Student found:", s)
        found = True
        break

if not found:
    print("Student not found")