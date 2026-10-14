'''
Create a class and object: Student details
Problem: Create a student class to store a student's name and roll number.Create an object and display the details using an instance method.
'''
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
Student1 = Student("Aman",97)
Student1.display()