#WAp to take an amount in rupees and calculate how many notes 500 and 100 rupee notes are needed.
a = int(input("Enter amount in Rupees: "))
notes_500 = a//500
notes_100 = (a%500)//100
print(f"500 Rupee Notes: {notes_500}, 100 Rupee Notes: {notes_100}")