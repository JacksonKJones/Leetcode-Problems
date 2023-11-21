class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = {}
        
        for i in nums:
            temp = i - self.reverse(i)
            
            if temp in numbers:
                numbers[temp] += 1
            else:
                numbers[temp] = 1
        
        result = 0
        modulo = 1000000007
        for value in numbers.values():
            result = (result % modulo + (value * (value - 1) // 2)) % modulo
        
        return int(result)
        
    def reverse(self, number):
        revnum = 0
        while number > 0:
            revnum = revnum * 10 + number % 10
            number //= 10
        return revnum   