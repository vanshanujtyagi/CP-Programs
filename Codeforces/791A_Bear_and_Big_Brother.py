#Asks the user for values of a and b, which are ages of Limak and Bob respectively. #input().split() splits the string and map() converts it into int.
a,b=map(int,input().split())
for year in range(1,1001): #very long range
    a=3*a
    b=2*b
    if a>b: #when age of Limak is greater than Bob.
        print(year)
        break
