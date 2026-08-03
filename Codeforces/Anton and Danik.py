n=int(input()) #input the number of games
s=input() #input the string
if s.count('A')>s.count('D'): # iterable.count("specific") functions counts for a specific element in a iterable.
    print("Anton")
elif s.count('A')<s.count('D'):
    print("Danik")
else:
    print("Friendship")
