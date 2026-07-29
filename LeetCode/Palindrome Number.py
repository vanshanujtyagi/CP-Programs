class Solution: #leetcode default
    def isPalindrome(self, x: int) -> bool: #leetcode default int variable x
        y = str(x) #converts int x into a string and stores string into a variable y
        z = y[::-1] #strings are slicable and indexed. No defined starting, stop index but -1 as steps that means moving backwards.
#z now is the backward version of input int x in string form.
        if y == z: 
            return True
        else:
            return False
