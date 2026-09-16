'''
wap to input marks of n stds in a list.display highest marks,lowest marks,avg,ang no. of stds who passed.
'''
n = int(input("Enter no. of students: "))
marks = []
for i in range(n):
    marks.append(int(input("Enter Marks: ")))

print("Lists: ",marks)
print("Highest: ",max(marks))
print("Lowest: ",min(marks))
print("AVg Marks: ",sum(marks)/n)

passed = 0

for m in marks:
    if m >= 40:
        passed += 1

print("Passed students:", passed)