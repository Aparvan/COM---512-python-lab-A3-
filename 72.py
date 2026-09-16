'''
wap to input marks of 10 stds. store only valid marks b/w 0 and 100 in a list.skip invalid marks.
'''
marks = []
for i in range(10):
    m = int(input("Enter marks of students: "))
    if m>=0 and m<=100:
        marks.append(m)
    else:
        print("Invalid marks")
        continue
print("Valid", marks)