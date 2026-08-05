n=int(input()) #take the value for n in sequence. eg 7, -1+2-3+4-5+6-7
if n%2==0: #if n is even, then int number of pairs can be made and each pair results in 1.
    print(n//2) #so n//2 gives how many times 1 is recieved. 
else: #if n is odd, then int number of pairs + one extra number is left which is -n. eg, (-1+2)(-3+4)(-5+6)-7
    print((n//2)-n) #thus n//2 gives how many times 1 is recieved and -n is the extra number.
