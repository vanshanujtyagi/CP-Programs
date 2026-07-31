class Solution:
    def mySqrt(self, x: int) -> int: #leetcode default for x=int(input())
        if x == 0: #if x is 0, then its sqrt is 0. 0 is an exceptional case in the following mechanism
            return 0 #print 0 as it is the sqrt of 0
        elif x == 1: #if x is 1, then its sqrt is 1. 1 is an exceptional case in the following mechanism
            return 1 #print 1 as it is the sqrt of 1
        else: #main mechanism starts from here
            for i in range(x+1): # x+1 to compensate for the loss of 1 in end limit during iteration
                if i * i > x: #if square of i is greater the input number x, that means the number behind it, is the sqrt ans of x
                    return i - 1 #print the preceeding number of i
#eg. x=47, then 7*7>47 that means the number preceeding would be the sqrt ans ie 6
#eg. x=25, then 6*6>25, that means the number preceeding would be the sqrt ans ie 5
