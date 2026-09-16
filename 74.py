'''
WAp to input a list of nod. and create a new list containing only unique elem.
'''
list = []
n_list = []
n = int(input("Enter number: "))
for i in range(n):
    x = int(input("Enter number: "))
    list.append(x)

for x in list:
    if x not in n_list:
        n_list.append(x)
print(n_list)