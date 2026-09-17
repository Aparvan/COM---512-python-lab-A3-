'''
wap to input nos. in a list and create 2 separate lists for even snd odd no.
'''
even_list = []
odd_list = []
n = list(map(int,input("Enter a number: ").split()))
for i in n:
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
    
