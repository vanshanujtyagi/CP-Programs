n,t=map(int,input().split())
queue=list(input())
for j in range(0,t):
    skip=False
    
    for i in range(0,n-1):
        if skip:
            skip=False
            continue 
        if queue[i]=='B' and queue[i+1]=='G':
            queue[i]='G'
            queue[i+1]='B'
            skip=True
print("".join(queue))
    
