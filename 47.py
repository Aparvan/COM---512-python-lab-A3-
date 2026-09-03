#wap to take a pass and check len,presence of@, and whether first and last chars are diff
password = input("Enter a password: ")
print((len(password) >= 8) and (password.find("@") != -1) and (password[0] != password[-1]))
