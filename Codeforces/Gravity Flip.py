n = int(input()) #inputs the number of columns
cubes = list(map(int, input().split())) #takes values of number of cubes in each row
cubes.sort() #sort all values of cubes, by default increasing order
print(*cubes) # *iterable is called unpacking operator, this unpacks a list into into elements separated by spaces, no commas, no brackets.
#in the question the logic was to sort the number of cubes in columns in ascending order as the gravity is rightwards. 
