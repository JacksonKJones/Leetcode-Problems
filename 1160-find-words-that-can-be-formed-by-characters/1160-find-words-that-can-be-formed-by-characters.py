class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counts = [0] * 26
        ans = 0
        
        for ch in chars:
            counts[ord(ch) - ord('a')] += 1
            
        for word in words:
            if self.canForm(word, counts):
                ans += len(word)

        return ans

    def canForm(self, word, counts):
        c = [0] * 26
        
        for ch in word:
            x = ord(ch) - ord('a')
            c[x] += 1
            if c[x] > counts[x]:
                return False

        return True