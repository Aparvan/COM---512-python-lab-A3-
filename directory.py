#write a python program to print the contents of a directory using the os module
import os

directory = r"C:\Users\sharm\OneDrive\python.lab\python(A3)"

files = os.listdir(directory)
print(files)