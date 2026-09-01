#WAP to take a std name and roll mo. , then generate a username using the first 3 letters of name and last 2 digits of roll no.
name = input("Enter yor name: ")
roll_no = input("Enter roll no: ")
username = name[:3]+roll_no[-2:]
print("Username: ",username)