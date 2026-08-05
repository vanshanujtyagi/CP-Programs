n = int(input()) #take input for the number of rooms.
count = 0 #initial count 0
for i in range(n): 
    p, q = map(int, input().split()) #first input int is p and second is q. Here, p denotes number of students and q denotes the capacity.
    if q - p >= 2: #if q-p or capacity-students is greater than or equals to 2.
        count += 1 #increase count by 1
print(count)
