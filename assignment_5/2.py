a=int(input("Enter a Number: "))
print("The table of %d is: "%a)
for i in range(1,11):
    print("%d * %d = %d"%(a,i,a*i))
    i=i+1