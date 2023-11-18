class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse = 0
        temp = x

        while temp != 0:
            num = temp % 10
            reverse = reverse * 10 + num
            temp //= 10

        return reverse == x