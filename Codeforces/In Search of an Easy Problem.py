n=int(input())
responses=list(map(int,input().split()))
if 1 in responses: #if 1 is in responses
    print("HARD")
else: #if there is no 1 in responses, then for sure, it has only zeroes.
    print("EASY")
