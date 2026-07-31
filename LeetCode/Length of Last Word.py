class Solution:
    def lengthOfLastWord(self, s: str) -> int: #leetcode default to s=input()
        words=s.split() #converts the string into list of strings with separtion of spaces.
        length=len(words) #finds the length of list ie. how many word are present in the sentence.
        return len(words[length-1]) #length-1 is the index of the last word. hence print its length.
        
        
