t=int(input())
n=[]
for i in range(0,t): #taking inputs
    n.append(int(input()))

for i in range(0,t): 
    k=len(str(n[i])) #length of the call answerer's number
    print(((n[i]%10)-1)*10+((k*(k+1))//2)) #final answer
