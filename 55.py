#wap  a python prog to detect whether a comment is spam or not. A comment shoulkd be treated as spam if it contains any of these words
comm = input("enter comment: ")
spam_keyword = ["make a lot of money ","buy this","subscribe this","click this"]
is_spam = False
for spam_keyword in spam_keyword:
    if spam_keyword in comm:
        print("Comment is spam")
        is_spam = True
        break
else:
    print("Comment is not spam")