a=int(input("Enter The Value of N: "))
print("Eirst N odd natural numbers in reverse order is:",end=" ")
for i in range(0,a):
    if(a%2!=0):
        print(a,end=" ")
    a=a-1