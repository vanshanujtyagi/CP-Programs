n=int(input())
scores=list(map(int,input().split()))
maximum=scores[0] #initial maximum score is the first one.
minimum=scores[0] #initial minimum score is the first one.
count=0 #initial count is 0.
for i in range(1,len(scores)): #loop for all indexes of list scores, starting from 1.
    if scores[i]>maximum: #if value at index i, starting from 1, is greater than the maximum, initially the first value.
        count+=1 #increase the count.
        maximum=scores[i] #new maximum is the value at the i index.
    elif scores[i]<minimum: #if value at index i, starting from 1, is smaller than the minimum, initially the first value. 
        count+=1 #increase count.
        minimum=scores[i] #the new minimum is the value at the i index.
print(count) #print count.
