#wap that asks the nuser to enter a username and paassword.the user should get only 3 attempts . if the correct credentials are enterd , display "login succeessfully" and stop the loo. if all attempts are useed, "display"Account locked"
user0 = "RajuMistri"
passw = "123456"
for i in range(3):
    user = input("enter a username: ")
    password = input("enter a password: ")
    if user0 == user and passw == password:
        print("Login Successfull")
        break
    else:
        print("Invalid Credentials, try again")
else:
    print("Account Locked")