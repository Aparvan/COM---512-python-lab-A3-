'''
wap to check whether a no. is perfect no. NO. IS perfect if the sum of its proper divisor is equal to nu. itself
'''

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")
