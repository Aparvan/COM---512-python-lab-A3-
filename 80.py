'''
wap to store 2 points as tuples and calculate the distance b/w them.
'''
t1 = (2,3)
t2 = (3,4)
x = t2[0]-t1[0]
y = t2[1]-t1[1]
distance = pow(x*x+y*y,0.5)
print(distance)