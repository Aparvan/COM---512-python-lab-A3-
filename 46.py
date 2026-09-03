#WAp take name,branch,year. generate a code name using str concatenation and slicing and repetition.
name = input("Enter name: ")
branch = input("Enter branch: ")
year = input("Enter year: ")
code_name = name[0:3]+"-"+branch[0:3]+"-"+year[-2:]
print("*" *30)
print(code_name)
print("*" *30)