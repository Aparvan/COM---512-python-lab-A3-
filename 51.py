#wap to calculate the final bill amt after applying a discount . the prog should take the total bill amt as input from user and apply the discount acc to following rules. After calculating the discount, the prog should display the discount amount and the final bill amt payable by the customer.
#bill amt   Discount
#Above 5000     20%
#3000-5000       10%
#below 3000      no discount
bill_amt = float(input("Enter bill amt: "))
if bill_amt > 5000:
    discount = .20
elif bill_amt>=3000 and bill_amt<=5000:
    discount = .10
else:
    discount = 0
disc = bill_amt*discount
final_amt = bill_amt-disc
print(disc)
print(final_amt)