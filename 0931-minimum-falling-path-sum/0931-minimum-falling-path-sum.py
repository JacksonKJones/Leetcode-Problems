class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        l = len(matrix);
        minSums = [0] * l;
        for i in matrix:
            g = [0] * l;
            for j, k in enumerate(i):
                m, n = max(0, j-1), min(l, j+2);
                g[j] = min(minSums[m:n]) + k;
            minSums = g;
        return min(minSums)