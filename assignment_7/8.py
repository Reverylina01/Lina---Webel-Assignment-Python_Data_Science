str=input("Enter a String: ")
i=0
str_1=""
for x in str:
    if str.index(x)==i:
        str_1+=x
    i+=1
print(str_1)    
    
