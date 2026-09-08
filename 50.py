#wa p to simulate a digital lock system
#the lock should be ask the user to enter a 4 dig pin. if the entered pin does not contain exactly 4 dig, the prog should display an error mesg and ask again . if the the enterd pin is correct, the lock should open. otherwise, the prog should ask the user to try again.
pin = input("Enter pin: ")
correct_pin = "1234"
if len(pin)!=4 and pin.isdigit():
    print("PIN must exactly 4 ")
elif pin == correct_pin:
    print("PIN is correct. The lock is open.")
else:
    print("Error msgg, Ask again")
