'''
Instance methods: Rectangle area and perimeter
Problem: Create a rectangle class with length and breadth. Use instance methods to calculate its area and perimeter.
'''
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

Rect1 = Rectangle(5,10)
print("Area: ", Rect1.area())
print("Perimeter: ", Rect1.perimeter())