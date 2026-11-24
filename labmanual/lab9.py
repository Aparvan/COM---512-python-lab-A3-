"""
Experiment 9: Employee Management System Using Inheritance
Question / Aim:

Write a Python program to implement an Employee Management System using inheritance.
"""
class Employee:
    def __init__(self, name, empid, salary):
        self.name = name
        self.empid = empid
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.empid)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, empid, salary, department):
        super().__init__(name, empid, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


m1 = Manager("Rahul", 101, 50000, "IT")

print("Employee Management System")
m1.display()