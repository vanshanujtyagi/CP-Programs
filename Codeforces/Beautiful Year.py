y=int(input()) #takes the input year in int. eg 1987
while len(set(str(y+1)))!=4: #run the loop while the number of distinct digits of y+1 ie the next year is not equal to 4. eg 1988 runs in the loop.
    y+=1 #now y=1988
print(y+1) #prinnt the next year. eg for y=2012, loop runs but for 2013 it doesnt, but y is still 2012. 
