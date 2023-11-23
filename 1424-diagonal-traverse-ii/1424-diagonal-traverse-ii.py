class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        diagonals = [deque() for i in range(len(nums) + max(len(row) for row in nums) - 1)]
        for row_id, row in enumerate(nums):
            for col_id in range(len(row)):
                diagonals[row_id + col_id].appendleft(row[col_id])
        return list(chain(*diagonals))

       







