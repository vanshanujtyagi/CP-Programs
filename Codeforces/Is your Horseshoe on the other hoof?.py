colors=list(map(int,input().split())) #take input
print(4-len(set(colors))) #len(set(colors)) identies and creates a set of distinct elements(colors) and finds its length ie the number of distinct colors.
#4-len(set(colors)) find how many more colors are missing to make all the four distinct.
