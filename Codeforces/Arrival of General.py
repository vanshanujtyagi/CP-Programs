n = int(input()) #take the input of number of soldiers
s = list(map(int, input().split()))  #make list of heights of soldiers

maxindex = s.index(max(s)) #give the index of the maximum height
minindex = n - 1 - s[::-1].index(min(s)) #give the index of the minimum height, reversed the string so that we can find the index of last value in case of repeated occurence of same value.

if maxindex > minindex: #if maxindex is greater than minindex, both will swap each other at some time.
    print(maxindex + (n - 1 - minindex) - 1) #thats way -1 to compensate.
else: 
    print(maxindex + (n - 1 - minindex))
