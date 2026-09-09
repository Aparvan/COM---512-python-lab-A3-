'''
wap to input a no. and check whether it is a prime or not. A no. is prime if it has no divisior other than 1 and itseld
'''
n=int(input("Enter a no: "))
for i in range(2,n//2+1):
    if not n%i:
     print(f"{n} not prime")
     break
else:
    print(f"{n} prime")