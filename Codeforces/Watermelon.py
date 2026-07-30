w=int(input()) #inputs the int w, in question it is guranteed 1<=w<=100
if w%2==0 and w!=2: #if w is even (it can be divided into positive even parts) except 2
    print("Yes")
else: #odds cant be divided into two positive even parts.
    print("No")
