def coprime(a,b):
    
    x = 1

    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            x = i

    return x == 1
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

if coprime(first, second):
    print('%d and %d are CO-PRIME' %(first, second))
else:
    print('%d and %d are NOT CO-PRIME' %(first, second))
