class Solution(object): 
    def twoSum(self, nums, target): #leetcode default for input variable list nums
      for i in range(len(nums)): #check for all values of positional indices of list nums
            for j in range(i+1,len(nums)): #check for range(i+1, lens(nums)) ie j in starting: next integer to i and ending: last positional index of nums.
                if nums[i]+nums[j]==target: #if nums[i]+nums[j]==target ie. nums[i] and nums[j] cannot be same elements due to the above conditions.
                    return i,j #print(i,j)
                    break #break the loop after finding only one solution since only one solution is asked.
