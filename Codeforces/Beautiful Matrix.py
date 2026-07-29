matrix=[] #matrix is a list, which will, become a list of lists in further steps.
for i in range(5): #loop will run 5 times as we are asked to store a 5x5 matrix, storing 5 lists.
    values=list(map(int,input().split())) #user will enter as string containing digits separated by space, they would be converted into int and later groupped into list.
    matrix.append(values) #append the list formed above containing 5 elements in the matrix, as the loop runs 5 time, 5 lists containing 5 elements are stored in matrix.
for i in range(5): #check for each value of row
    for j in range(5): #check for each value of column
        if matrix[i][j]==1: #check whether element is 1 or not
            row=i #if yes then store row index as row
            col=j #if yes then store column index as column
print(abs(2-row)+abs(2-col)) #abs(2-row) and abs(2-col) give vertical and horizontal distances to the centre(2,2).
#abs(2-row)+abs(2-col) is the total steps.
