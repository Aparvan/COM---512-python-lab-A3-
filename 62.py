'''
wap to print nos from 1 to 50 , but skip all nos divisible by 4.
'''
for i in range(1,50):
    if i%4 == 0:
        continue
    print(i,end =" ")