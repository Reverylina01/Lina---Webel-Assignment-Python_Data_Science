a = int(input ("Enter The First Number: "))  
b= int(input ("Enter The Second Number: "))  
  
print ("The Prime Numbers in the range are: ")  
for x in range (a,b + 1):  
    if x > 1:  
        for i in range (2, x):  
            if (x % i) == 0:  
                break  
        else:  
            print (x)  