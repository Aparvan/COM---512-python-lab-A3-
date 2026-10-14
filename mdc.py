'''
wac tain which has methods too book a ticket,get status and get fare information of train running under indian railways.

'''
class Train:
    def ___init__(self,seats,fare):
        self.seats = seats
        self.fare = fare

    def book_tickets(self):
        self.seats -= 1
        if self.seats>0:
            print("ticket is booked")
        else:
            print("not booked")
    def status(self):
        print("No. of seats: ",self.status)
    def fare(self):
        print("Price: ",self.fare)

train1 = Train(10,90)
train1.book_tickets()
train1.status()
train1.fare()