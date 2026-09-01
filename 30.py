# #WAp to take an email address and print domain name
# email = input("Enter your email: ")
# domain = email.split("@")
# print("Domain name: ",domain[1])
email = input("Enter your email: ")
index = email.find("@")
domain = email[index+1:]
print("Domain name: ",domain)