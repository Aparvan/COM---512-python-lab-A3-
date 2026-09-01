# #WAp a python program to take a std's full name and display:
# total no. of chars
# 1st char
# last char
# Name in upper case

name = input("Enter full name: ")
print("Total no. of char: ",len(name))
print("1st char: ", name[0])
print("Last char: ", name[-1])
print("Name in upper case: ", name.upper())
