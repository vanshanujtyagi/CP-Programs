n=int(input()) #asks for the number of the problems
count=0
for i in range(n): #n lines
    a,b,c=map(int,input().split()) #if Petya, Vasya, Tonya are sure or unsure
    if a+b+c>=2:
        count=count+1 #counts the problem if above cond. holds true
print(count)
