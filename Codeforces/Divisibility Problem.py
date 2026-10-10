n=int(input())
a=[]
b=[]
for i in range(0,n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in range(0,n):
    if a[i]!=b[i]:
        if a[i]%b[i]!=0:
            steps=b[i]*((a[i]//b[i])+1)-a[i]
        else:
            steps=0
    else:
        steps=0
    print(steps)
