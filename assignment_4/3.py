def prime(a):
    for i in range(1,a+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,end=" ")
x=int(input("Enter the Value of N: "))
print("First N prime Number:",end=" ")
prime(x)
