'''
wap to input a no.and reverse it using arithmetic operation only.
'''

n = int(input("enter a no: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse number is:", reverse)
