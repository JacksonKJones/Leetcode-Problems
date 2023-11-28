class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        seats = 0
        plants = 0
        ans = 1
        mod = 1000000007
        
        for i in corridor:
            if i == 'S':
                seats += 1
            if seats == 2 and i == 'P':
                plants += 1
            if seats == 3:
                ans *= (plants + 1)
                ans %= mod
                seats = 1
                plants = 0
        
        if seats < 2: return 0
        return ans