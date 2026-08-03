players=input() #take string input, as per the question, the input contains combination of 1 and 0 in string type.
if '1111111' in players or '0000000' in players: #if 7 ones substring or 7 zeroes substring are present in players string.
    print("YES") #print yes
else: #if not present
    print("NO") #print no
