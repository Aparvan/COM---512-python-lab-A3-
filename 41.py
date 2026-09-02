#Take an email addess and check whether it contains @ and .com
email = input("Enter email: ")
print(email.find("@"))
print(email.endswith(".com"))