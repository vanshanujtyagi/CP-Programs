username=input() #ask for input string
distinct=len(set(username)) #set is a data type that stores only distinct values in {}. In a string, it stores individual unique elements.
# Using set here, so that we can obtain only distinct values. then finding the length of the set obtained ie the number of distinct letter.
if distinct%2==0: #if it is even, she is a female
    print("CHAT WITH HER!") #print chat with her.
else: #otherwise, it is odd and he is male
    print("IGNORE HIM!") #print ignore him.
