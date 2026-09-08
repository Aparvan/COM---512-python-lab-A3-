#wap to input marks of 5 std. for each std, the prog should check whether the entered marks are valid or invalid. marks are considered valid only if the are b/w 0 and 100. if the 
for i in range(1,6):
    m = float(input("enter marks: "))
    if 0 <= m >=100:
        print("valid marks")
        continue
    else:
        print("Invalid marks")