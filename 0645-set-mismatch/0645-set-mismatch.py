class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        repeating_num = 0
        lost_num = 0
        
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                repeating_num = i
            elif count == 0:
                lost_num = i
            if repeating_num > 0 and lost_num > 0:
                return [repeating_num, lost_num]