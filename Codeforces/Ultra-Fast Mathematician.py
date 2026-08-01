num1=input() #input the number, but in string type as it is iterable ie loop can run on strings but not int
num2=input() #input the second number
result=[] #empty list result
for i in range(len(num1)): #loop for all digits of number. len(num1) is the number of digits in num1==num2 
    if num1[i]==num2[i]: #if corresponding digits of both numbers are equal
        result.append('0') #then, append 0 in the result
    else: #if they are not equal
        result.append('1') #append 1 in the result
print(("").join(result)) #("").join(result) will join all the elements of the list result using the separtor "" which is essentially no space.
