n=int(input())
coins=list(map(int,input().split()))
coins.sort(reverse=True)
total=0
count=0
remaining=sum(coins)
for i in coins:
    total+=i
    remaining-=i
    count+=1
    if total>remaining:
        break
print(count)
