#WAp a program to calculate SImple Interest and total amount using formula SI = (P*R*T)/100 using
#Principal,Rate, and Time entered by the user

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
SI = (P*R*T)/100
Total_Amount = P + SI
print("simple Interest = ", SI)
print("Total Amount = ", Total_Amount)