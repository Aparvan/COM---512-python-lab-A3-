#wap to create record of n std. store each std-
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Roll number: ")
    name = input("Name: ")
    branch = input("Branch: ")
    marks = float(input("Marks: "))

    if roll not in students:
        students[roll] = [name, branch, marks]

roll = input("Enter roll number to search: ")

if roll in students:
    print(students[roll])
else:
    print("Student not found")  