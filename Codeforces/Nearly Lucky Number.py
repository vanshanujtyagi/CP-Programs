n=input()
result='YES' #default flag variable
count=n.count('4')+n.count('7') #counts total occurence of both 4 and 7
for digit in str(count): #check for each element in string count, ie. in 18 1 and 8 
    if digit not in '47': #check whether the above digits ie 1 and 8 not in 47
        result='NO' #change flag variable to NO
print(result)
