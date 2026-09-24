'''
wap to check whether a given program is present in a tuple. if the present, displayits position.
'''
val = (10,20,30,40,50,60,70,80,90,100)
n = int(input("enter val: "))
if n in val:
    print("Pos: ",val.index(n))
else:
    print("Val not found")  