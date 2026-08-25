#WAp to take a 2 digit number as input and print the sum of its digits
a = int(input("Enter 2-digit Number: "))
sum = (a//10) + (a%10)
print(f"Sum of Digits: {sum}")