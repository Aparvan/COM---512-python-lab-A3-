'''
wap to show that tuple values cannot be changed directly.Convert tuple into two list,update it and convert it back into tuple.
'''
val = ([1,2],[4,5])
lst1 = list(val[0])
lst2 = list(val[1])

lst1.append(3)
lst2.append(7)

val = tuple((lst1,lst2))
print(val)