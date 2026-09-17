'''
wap to count how many times a particular element
appears in a list.
'''

list = []
n = int(input("Enter number: "))
for i in range(n):
    list.append(int(input("Enter element: ")))
x = int(input("Enter element to count: "))
count = 0
for i in list:
    if i == x:
        count += 1
print("Count:", count)