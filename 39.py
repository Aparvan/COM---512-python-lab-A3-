#WAp to take a password and check whether it contaoins @ and has atleast 8 char.
password = input("Enter a password: ")
print((password.find("@") != -1) and (len(password) >= 8))