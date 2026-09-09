'''
#wap to input a decimal no. and convert it into binary without using the built-in function
'''

n = int(input("Enter a number: "))
binary = ""

while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2

print("Binary number is:", binary)  