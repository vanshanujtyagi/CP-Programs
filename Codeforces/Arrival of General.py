n = int(input())
s = list(map(int, input().split()))

maxindex = s.index(max(s))
minindex = n - 1 - s[::-1].index(min(s))

if maxindex > minindex:
    print(maxindex + (n - 1 - minindex) - 1)
else:
    print(maxindex + (n - 1 - minindex))
