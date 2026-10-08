n=input()
current=1
maximum=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        current=current+1
    else:
        current=1
    maximum=max(current,maximum)
print(maximum)
