class Solution: #leetcode default
    def runningSum(self, nums: List[int]) -> List[int]: #leetcode default for nums=list(map(int,input().split())) ie list of integer values
        summ=0 #initial sum 0
        for i in range(len(nums)): #runs the loop for (length of the list) times 
            summ=summ+nums[i] #adds index-wise elements to the existing sum. 
            nums[i]=summ #changes the value of element to the existing sum.
        return nums #leetcode default for print(nums)
