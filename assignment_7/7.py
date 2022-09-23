
str = input("Enter the string: ")
str = str.casefold()
rev_str = reversed(str)
if list(str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
