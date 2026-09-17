'''
WAp to input two lists and create a third list containing common elements.
'''
l1 = []
l2 = []
l3 = []
n = int(input("Enter list: "))
for i in range(n):
    l1.append(int(input("Enter element: ")))
n = int(input("Enter size of second list: "))
for i in range(n):
    l2.append(int(input("Enter element: ")))
for i in l1:
    if i in l2:
        l3.append(i)
print("Common elements:", l3)