x=int(input()) #inputs for a int x
remainder=x%5 #finds the remainder when divided by 5
if remainder==0: #if x is divisible by 5
    steps=x//5 #count how many times 5 can make x as it is perfectly divisible by 5
    print(steps) #that many times is the number of steps
else: #if not perfectly divisible by 5 and leaves a remainder in doing so, eg. 38%5=3
    num=x-remainder #find the number within x divisible by 5, eg. 38-3=35
    print((num//5)+1) #num//5 gives how many steps of 5, eg. 35//5=7 steps 
#and the extra number(remainder) eg. 3 will be divisible by 1,2,3,4 steps, hence add+1.
