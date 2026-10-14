'''
Create a Product class with name, price and quantity. Add an instance method to calculate the total cost of the product (price * quantity). Create an object of the Product class and display the total cost using the instance method.Take these values from the user and display the product name and total cost
'''
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price*self.quantity

name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enetr quantity: "))

product1 = Product(name,price,quantity)

print("Product: ",product1.name)
print("Total: ",product1.total_cost())
