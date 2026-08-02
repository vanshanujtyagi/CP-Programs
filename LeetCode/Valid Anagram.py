class Solution:
    def isAnagram(self, s: str, t: str) -> bool: #leetcode default for s,t=map(str,input().split()) 
        return sorted(s)==sorted(t) #print(sorted(s)==sorted(t)), if sorted(s)==sorted(t), then print True, else print False
      #sorted(iteration) function would sort all items of the iteration and store it in a list.
        
