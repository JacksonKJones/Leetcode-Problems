class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        ans = 0
        for i in range(l - 1, 0, -1):
            if nums[i] != nums[i-1]:
                ans += l - i
        return ans