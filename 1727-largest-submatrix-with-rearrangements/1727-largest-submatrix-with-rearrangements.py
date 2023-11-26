class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
                    
        ans = 0
        
        for i in matrix:
            i.sort(reverse=True)
            for j in range(len(matrix[0])):
                ans = max(ans, i[j] * (j + 1))
        
        return ans