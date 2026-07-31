n=int(input()) #take input the number of words
words=[] #empty list words
result=[] #empty list result
for word in range(n): #to run the loop n times, as to take n string inputs in n lines
    input_words=input() #take str input in input_words 
    words.append(input_words) #append input_words to words list
for word in words: #now, to check for each word in words list
    if len(word)>10: #if the length of word is strictly greater than 10
        result.append(word[0]+str(len(word)-2)+word[-1]) #append (first letter of word concat str(length of word-2) concat last letter of word) to the result list
    #this is beacuse, only strings can be concatenated with each other to form a greater string. len(word) is a integer and thus needs to be converted into a string.
    else: #if length of the word less than or equal to 10
        result.append(word) #append it as it is in the result list
for word in result: #for each word in result list
    print(word) #print the word
