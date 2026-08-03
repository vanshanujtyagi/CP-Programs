fiends,fence=map(int,input().split()) #take the inputs for number of friends and the height of the fence.
heights=list(map(int,input().split())) #take the input of heights of the friends in a list.
count=0 #default road width
for i in heights: #check for each height
    if i>fence: #if height of a friend is greater than the fence
        count+=2 #increase 2 to the count
    else: #if the height of the friend is lesser than or equals to the fence
        count+=1 #increase 1 to the fence
print(count) #print count ie the minimum road width
