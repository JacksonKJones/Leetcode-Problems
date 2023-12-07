class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        count = len(num)
        for i in reversed(num):
            if int(i) % 2 != 0:
                return num[:count]
            count -= 1
        return ""