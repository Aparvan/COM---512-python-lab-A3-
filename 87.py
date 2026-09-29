'''
wap to input a std's marks in n consecutive tests and store them in a list.Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.
Display the sequence,its length,and its staeting and ending tesgt numbers as a tuple.If multiple sequence have the same maximum length, display the first one.
MArks:[55,60,68,62,65,70,78,74]
Longest improving sequence:[62,65,70,78]
no. of tests:4
test range:(4,7)
conditions:
accept at lest one test
Equal marks break the improving sequence
Test numbers begin at 1
do not sort the list because the original order matters.
'''
n = int(input("Enter number of tests: "))
marks = []

for i in range(n):
    marks.append(int(input("Enter marks: ")))

start = 0
best_start = 0
best_length = 1

for i in range(1, n):
    if marks[i] <= marks[i-1]:
        start = i
        length = i-start+1
   

    if length > best_length:
        best_length = length
        best_start = start

sequence = marks[best_start:best_start+best_length]
test_range = (best_start+1,best_start+best_length)

print("Longest improving sequence:", sequence)
print("No. of tests:", best_length)
print("Test range:", test_range)