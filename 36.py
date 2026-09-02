#wap to take a word and print it in reverse order using slicing. Also check whether it is same forward and backward (palindrome) or not.
word = input("Enter a word: ")
print(word[::-1])
print(word == word[::-1])