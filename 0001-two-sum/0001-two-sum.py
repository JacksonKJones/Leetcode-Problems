class Solution(object):
    
    def twoSum(self, nums, target):
        
        '''
        I will check for the target by indexing the first integer in the array
        and then checking if it adds together with any of the other values to match
        the target. If it does not match, the code will repeat, starting with the next integer.
        '''
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]