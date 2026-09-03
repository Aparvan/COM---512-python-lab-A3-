#wap to take an emsil add and print username ,domain,and revrsed domain.
email = input("Enter your email address: ")
username = email.split("@")[0]
domain = email.split("@")[1]
rev_domain = domain[::-1]
print(username)
print(domain)
print(rev_domain)