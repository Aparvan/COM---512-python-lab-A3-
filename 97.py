'''
Q7. Employee Salary using Class
Create an Employee class that stores an employee’s name, basic salary, house rent allowance (HRA) percentage, 
travel allowance, and deductions. Add instance methods to calculate gross salary and net salary. Gross salary is the basic salary plus HRA and travel allowance. Net salary is gross salary minus deductions.
Display the employee’s name, gross salary, and net salary.
'''
class Employee:
    def __init__(self,name,basic_salary,hra_percentage,travel_allowance,deductions):
        self.name = name
        self.basic_salary = basic_salary
        self.hra_percentage = hra_percentage
        self.travel_allowance = travel_allowance
        self.deductions = deductions

    def gross_salary(self):
        hra_amount = (self.hra_percentage/100)*self.basic_salary
        return self.basic_salary + hra_amount + self.travel_allowance

    def net_salary(self):
        return self.gross_salary() - self.deductions
    