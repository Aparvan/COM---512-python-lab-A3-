'''
wap to perform searching activity using linear and binary search.-
'''
#5
a = [10, 20, 30, 40, 50]
x = int(input("Enter value: "))

# Linear Search
if x in a:
    print("Linear Search: Found")
else:
    print("Linear Search: Not Found")

# Binary Search
a.sort()
low, high = 0, len(a)-1
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

print("Binary Search:", "Found" if found else "Not Found")

