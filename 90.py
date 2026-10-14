'''
Create a class and objects: Student details
Problem:Create a std class to store a std's name and rollno's
'''
class Student:
    def __init__(self,name,rollno,branch,marks):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.marks = marks

    def display(self):
        print("NAME: ",self.name)
        print("RollNo: ",self.rollno)
        print("Branch: ",self.branch)
        print("Marks: ",self.marks)

Student1 = Student("RAju Mistri",15,"CSE",90)
Student1.display()