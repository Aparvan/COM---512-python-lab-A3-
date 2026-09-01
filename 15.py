#WAP to take two inputs a nd b , swap their values using a temporary variable and print updated values.
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
temp = a
a = b
b = temp
print(f"Updated value of a: {a}, Updated value of b: {b}")