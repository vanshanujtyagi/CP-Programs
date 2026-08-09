n=int(input())
scores=list(map(int,input().split()))
maximum=scores[0]
minimum=scores[0]
count=0
for i in range(1,len(scores)):
    if scores[i]>maximum:
        count+=1
        maximum=scores[i]
    elif scores[i]<minimum:
        count+=1
        minimum=scores[i]
print(count)
