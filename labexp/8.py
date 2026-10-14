#create a databse using lists and tuples-
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")

    if any(s[0] == roll for s in students):
        print("Roll number already exists")
        continue

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    students.append((roll, name, branch, cgpa))

print("\nStudent Database:")
for s in students:
    print(s)

roll = input("\nEnter roll number to search: ")

for s in students:
    if s[0] == roll:
        print("Student found:", s)
        break
else:
    print("Student not found")