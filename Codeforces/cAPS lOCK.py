word=input() #take the word
if word.isupper(): #if the word is entirely uppercase, then it is accidental.
    print(word.lower()) #change the word to lowercase
elif word[1::].isupper(): #if the word except the first letter is upper and the first letter is lower.
    print(word[0].upper()+word[1::].lower()) #change the respective cases
elif len(word)==1 and word.islower(): #if the word is a single digit and the word is entirely lowercase, then itsnt accidental.
    print(word.upper()) #change the letter to uppercase.
else: #if any other case
    print(word) #return the word as it is
        
