n=int(input())
statements=[]
count=0
for i in range(n):
    statements.append(input())
for j in statements:
    if '+' in j:
        count+=1
    else:
        count-=1
print(count)
