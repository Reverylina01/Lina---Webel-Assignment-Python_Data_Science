
words = input("Enter three words: ")
word = words.split()
word.sort()
new = ""
for x in word:
    new += x + " "
print(new)
