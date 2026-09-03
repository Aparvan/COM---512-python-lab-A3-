#take std fullname,rollno.genertae email usinf 1st 3 letters of 1st name,1st 3 letters of last name and and last 3 char of rollno
full_name = input("Enter name: ")
last_name = input("Enter last name: ")
roll_no = input("Enter roll no: ")
generate_email = full_name[0:3]+last_name[0:3]+roll_no[-3:]
print(generate_email)