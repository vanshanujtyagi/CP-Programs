n=int(input())
levels=[]
for i in range(1,n+1):
    levels.append(i)
levels=set(levels)
 
p,*parray=map(int,input().split())
q,*qarray=map(int,input().split())
 
sum=set(parray+qarray)
if sum==levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
