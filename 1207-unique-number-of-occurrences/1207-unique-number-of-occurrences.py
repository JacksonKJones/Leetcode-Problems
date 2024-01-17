class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort();
        counts = [1];
        n = 0;
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                counts[n] += 1;
            else:
                counts.append(1);
                n += 1;
        
        counts.sort();
        
        for i in range(1, len(counts)):
            if counts[i] == counts[i-1]:
                return False
            
        return True
