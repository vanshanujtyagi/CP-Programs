n=int(input()) #take the input from the user.
s=input() #take the input color config.
count=0 #initial count is 0
for i in range(1,n): #check for each colour in string s starting from 1 to end.
    if s[i-1]==s[i] : #check if previous and the next colors are same
        count+=1 #then increase count by 1.
print(count) #print count.
