#wap to create a simple pass validation system.
#A pass will be considered valid only if it has atleat 8 charc and contains the @ symbol.once the user enters a valid pass, the program should display "Pasword accepted." and stop.otherwise it should display "Weak pass.Ty again." and ask for the pass again.
password = input("Enter a password: ")
valid_pas = "123@4567"
if len(password)!=8 and "@" in password:
    print("Password Accepted")
else:
    print("Weak password.Try again")