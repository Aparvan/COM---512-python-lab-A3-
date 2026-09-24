'''
WAP to store all month names in a tuples.input a month number And display the crresponding month name.
'''

month = ("January","Febrary","March","April","May","June","July","August","September","October","November","December")
n = int(input("Enter a month:"))
if 1 <= n <= 12:
    print(month[n - 1])
else:
    print("Enter a month number from 1 to 12.")