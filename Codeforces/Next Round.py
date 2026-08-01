participants, kth_rank=map(int,input().split()) #split the intput by spaces, the default type is string, but map them in int type to participants and kth_rank respectively.
scores=list(map(int,input().split())) #split the input by spaces, the default type is string, but map them in int type and make a list and store it in scores.
kth_score=scores[kth_rank-1] #kth_score is the kth-rank-1 index value of scores list. ie for 3rd element, 3-1=2 index, value=scores[2]
advance=[] #empty list advance
for i in scores: #loop for all values of scores list, ie int values of scores list
    if (i)>=(kth_score) and (i)>0 : #if i>=kth_score and i is non-zero positive,
        advance.append(i) #then append the value i into the advance list
    else: #if it is less than kth_score or is 0 or -ve, then
        break #break the loop, as it is guranteed they are in non-increasing(descending) order and if one values is lesser, then all the next values are lesser.
print(len(advance)) #advance is a list of qualified scores, thus print how many participants in advance.
