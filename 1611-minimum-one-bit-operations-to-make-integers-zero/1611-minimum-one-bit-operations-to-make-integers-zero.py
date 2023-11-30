class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        while n:
            ans = -ans - (n ^ (n - 1))
            print(n)
            n &= n - 1
        return abs(ans)