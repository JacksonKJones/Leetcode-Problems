class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        x = int(num[0])
        ans = "-1"

        for i in range(1, len(num)-1):
            if x == int(num[i]) and x == int(num[i+1]) and int(ans) < int(num[i-1]*3) :
                ans = num[i-1]*3
            x = int(num[i])
        if len(ans) != 3:
            return ""
        return ans
            