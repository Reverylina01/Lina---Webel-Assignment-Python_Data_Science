myTuple = ([7, 8], [9, 1, 10, 7])
print("The original tuple is : " + str(myTuple)) 
tupSum = sum(list(map(sum, list(myTuple)))) 
print("The summation of tuple elements are : " + str(tupSum))