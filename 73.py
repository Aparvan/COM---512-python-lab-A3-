'''
wap to input no's ina list and find the second largest number.
'''
n = int(input("Enter a no: "))
list = []
for i in range(n):
    x = int(input("Enter a no: "))
    list.append(x)
    list.sort()
print("Second largest: ",list[-2])