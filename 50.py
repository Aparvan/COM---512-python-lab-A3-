#wa p to simulate a digital lock system
#the lock should be ask the user to enter a 4 dig pin. if the entered pin does not contain exactly 4 dig, the prog should display an error mesg and ask again . if the the enterd pin is correct, the lock should open. otherwise, the prog should ask the user to try again.
pin = input("Enter pin: ")
if len(pin)==4 and pin.digit():
    print("PIN is correct")
else:
    print("Error msgg, Ask again")