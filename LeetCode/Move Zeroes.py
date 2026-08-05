class Solution:
    def moveZeroes(self, nums: List[int]) -> None: #nums is a list of int
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums: #check in nums
            if i==0: #if the element i is zero
                nums.pop(nums.index(i)) #pop i from nums. pop(index) 
                nums.append(0) #append 0 in nums.
        
