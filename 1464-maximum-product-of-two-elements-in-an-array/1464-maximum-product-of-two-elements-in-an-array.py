class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 2:
            return (nums[0]-1) * (nums[1]-1)
        
        big = 0
        i = 0
        biggest = 0
        j = 0
        for x in range(len(nums)):
            if biggest <= nums[x]:
                big = biggest
                biggest = nums[x]
                i = j
                j = x
            elif big < nums[x]:
                big = nums[x]
                i = x
                
        return (nums[i]-1) * (nums[j]-1)
            