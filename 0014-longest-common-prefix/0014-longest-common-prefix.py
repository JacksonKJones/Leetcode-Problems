class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs[0]
        
        for i in strs[1:]:
            while i.find(ans) != 0:
                ans = ans[:-1]
        return ans