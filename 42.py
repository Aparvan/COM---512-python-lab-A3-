#wap a sentence contains double spaces and unwanted spaces at the begning or end.Clean the sentence
sentence = input("Enter a sentence: ")
sentence = " ".join(sentence.split())
print(sentence)