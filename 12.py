#WAP to take total minutes as input and convert it into hours and remaining minutes.
a = int(input("Enter total minutes: "))
hours = a//60
remain_minutes = a%60
print(f"Hours: {hours}, Remaining Minutes: {remain_minutes}")
