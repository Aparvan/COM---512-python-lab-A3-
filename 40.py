#wap to take a str and separate char present at even indx pos and odd indx pos
str = input("Enter a str: ")
even = str[::2]
odd = str[1::2]
print(f"Even: {even}, Odd: {odd}")