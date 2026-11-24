"""
Experiment 2: Iteration Over List and Dictionary
Question / Aim:

Write a Python program to illustrate iteration over a list and dictionary.
"""
# Iteration over a list

list1 = [1, 2, 3, 4, 5]

print("Iterating over the list:")

for item in list1:
    print(item, end=" ")

# Iteration over a dictionary

dict1 = {'a': 1, 'b': 2, 'c': 3}

print("\nIterating over the dictionary:")

for key, value in dict1.items():
    print(key, ":", value)