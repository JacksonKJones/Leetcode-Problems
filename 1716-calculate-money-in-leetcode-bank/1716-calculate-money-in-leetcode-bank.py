class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        days = 0
        add = 1
        bonus = 0
        while days < n:
            ans += add + bonus
            days += 1
            add += 1
            if add % 8 == 0:
                add = 1
                bonus +=1
        return ans
            
            