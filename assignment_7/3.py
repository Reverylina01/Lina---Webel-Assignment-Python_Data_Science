def reverse_string(s):
	str = ""
	for i in s:
		str = i + str
	return str
str=input("Enter a String: ")
print("The reversed string is : ", end="")
print(reverse_string(str))
