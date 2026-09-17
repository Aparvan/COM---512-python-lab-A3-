'''
wap to rotate a list one pos to the right.
'''
n = int(input("Enter number: "))
list = []
for i in range(n):
    list.append(int(input("Enter number: ")))
list = [list[-1]] + list[:-1]
print(list)