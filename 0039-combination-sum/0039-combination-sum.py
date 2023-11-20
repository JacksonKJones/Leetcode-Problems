class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(target, index, total):
            if target < 0:
                return
            if target == 0:
                ans.append(total)
                return 
            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, total + [candidates[i]])
        
        dfs(target, 0, [])
        return ans