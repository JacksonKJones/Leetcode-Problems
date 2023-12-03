class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        full1 = ''.join(word1)
        full2 = ''.join(word2)
        return full1 == full2  