#WAp to take a 10 digit mobile no. and display only last 4 digits.Replace the first 6 digits with ******.
mob_no = input("Enter your 10 digit mobile no: ")
last_4_dig = mob_no[-4:]
print("******"+last_4_dig)
#WAp to take a 10 digit mobile no. and display only last 4 digits.Replace the first 6 digits with ******.
mob_no = input("Enter your 10 digit mobile no: ")
first_6_dig = mob_no[:6]
print(first_6_dig.replace(first_6_dig,"******")+mob_no[-4:])   