"""
Experiment 5: Linear Search and Binary Search
Question / Aim:

Write a Python program to perform searching activity using Linear Search and Binary Search.

"""
a = [10, 20, 30, 40, 50]

x = int(input("Enter value: "))

# Linear Search

if x in a:
    print("Linear Search: Found")
else:
    print("Linear Search: Not Found")

# Binary Search

a.sort()

low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == x:
        found = True
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Binary Search: Found")
else:
    print("Binary Search: Not Found")