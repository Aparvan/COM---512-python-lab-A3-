#Wap to fill the given letter template with name and date.
# letter = ""
# Dear <Name>
# You are selected!
# <Date>
# ""

# name = input()
# date = input()
# letter = """
# Your are selected!
# """
# print(f"Dear {name},\nYou are selected!\n{date}")

letter = """
Dear <Name>,
You are selected!
<Date>
"""
name = input("Enter your name: ")
date = input("Enter the date: ")

letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)

print(letter)