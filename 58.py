'''
wap to input 2 no's and find their gcd using a loop.
'''
n = int(input("Enter a num: "))
n1 = int(input("enter a num1: "))
# for i in range(min(n,n1),0,-1):
#     if n %i == 0 and n1%i == 0:
#         print(f"GCG of {n} and gcd of{n1} is: {i}")
#         break
while n1:
    n, n1 = n1, n%n1
print(f"gcd: {n}")