#Take rollno like 2024a1r057 and extract admission year,program code, and roll no. digits using slicing.
roll_no = input("Enter roll no: ")
adm_year = roll_no[0:4]
prog_code = roll_no[4:6]
roll_dig = roll_no[-3:]
print(adm_year)
print(prog_code)
print(roll_dig)