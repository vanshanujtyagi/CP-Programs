s=input() #take string input from the user
lcount=0 
ucount=0
for i in s: #loop for each character in string s
    if i.isupper()==True: #if i is uppercase
        ucount+=1 #increase ucount by 1
    else: #if not uppercase, then lowercase
        lcount+=1 #increase lcount by 1
if lcount>=ucount: #if lcount equal to or greater than ucount
    print(s.lower()) #print the string in lowercase
else: #if lcount is lesser than ucount
    print(s.upper()) #print the string in uppercase
