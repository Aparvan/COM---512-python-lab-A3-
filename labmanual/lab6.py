"""
Experiment 6: Reverse Every Kth Row in a Matrix
Question / Aim:

Write a Python program to reverse every Kth row in a matrix.

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

k = int(input("Enter k: "))

for i in range(k - 1, len(matrix), k):
    matrix[i].reverse()

for row in matrix:
    print(row)