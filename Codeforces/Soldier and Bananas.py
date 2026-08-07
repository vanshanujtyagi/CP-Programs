k,n,w=map(int,input().split()) #input the values
cost=0
for i in range(1,w+1): #check for all values of w, which is the number of bananas needed
    cost=cost+(i*k) #the new cost is the previous cost plus i times k
print(max(0,cost-n)) #print the cost-n and if thats a negative value, print 0.
