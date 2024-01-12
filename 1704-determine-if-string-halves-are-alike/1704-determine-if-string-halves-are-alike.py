class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def vowel_count(string):
            vowels = set("aeiouAEIOU");
            return sum(1 for char in string if char in vowels);

        l = len(s)//2;
        

        a = s[:l];
        b = s[l:];

        return vowel_count(a) == vowel_count(b);