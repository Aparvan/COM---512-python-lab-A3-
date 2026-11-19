"""
WAP that creates a parkingTicket Class for calculating the parking fee for one vehicle.
The Program must:
1. Ask the user to enter the vehicle number and parking duration in hours.
   The Duration may include a fraction, such as 2.5 hours.
2. Calculate the fee using the billable hours:
    > Each started hour counts as one full hour. For example, 2.1 hours is billed as 3 hours.
    > Charge Rs.30 per billlable hour for the first two hours.
    > Charge Rs.20 for each billlable hour after the first two hours.
3. Display the vehicle number, actual parking duration, and total fee.
4. If the duration is zero or negative, display an error message and do not calculate a fee.

Example: A vehicle parked for 2.5 hours is billed for 3 hours.
         The fee is Rs.30 + Rs.30 + Rs.20 = Rs.80
"""

class Park:
    def __init__(self, vh_no, duration):
        self.vh_no = vh_no
        self.duration = duration

    def bill_cal(self):
        if self.duration <= 0:
            print("Parking Hours Can't be Negtive.")
            return 0

        billed_hrs = int(self.duration)

        if self.duration > billed_hrs:
            billed_hrs += 1

        total_bill = 0
        if billed_hrs <= 2:
            total_bill += billed_hrs * 30
        elif billed_hrs > 2:
            total_bill += (30 * 2) + ((billed_hrs - 2) * 20)

        return total_bill

    def display(self):
        if self.duration <= 0:
            self.bill_cal()
            return

        print("Vehicle Number :",self.vh_no)
        print("Parking Duration (in hrs) :",self.duration)
        print("Total Bill Amount :",self.bill_cal())

vh_no = input("Enter Vehicle Number : ")
duration = float(input("Enter Vehicle Parking Duration : "))

veh1 = Park(vh_no, duration)
veh1.display()