#wa pto determine whether a std is eligible for a scholarship.the scholarship should be granted if the stds satisfies either of the following conditions.
#a the std has a cgpa of 8.5 or above and attd of 85%
#b the std has won a national-level championship.
#the prog should take cgpa,attd and championship status as input and print whether the std is eligible for scholarship or not.
cgpa = float(input("Enter cgpa: "))
attendance = int(input("Enter Percentage: "))
status = input("Won a national-level championship: ").strip().lower()
flag = False
if(status == "true"):
    flag = True
if cgpa >= 8.5 and attendance >= 85 or flag:
    print("Eligible")
else:
    print("Not Eligible")