class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        location = points[0]
        ans = 0
        for i in range(1, len(points)):
            while location[0] > points[i][0] and location[1] > points[i][1]:
                location[0] -= 1
                location[1] -= 1
                ans += 1
            while location[0] > points[i][0] and location[1] < points[i][1]:
                location[0] -= 1
                location[1] += 1
                ans += 1
            while location[0] < points[i][0] and location[1] > points[i][1]:
                location[0] += 1
                location[1] -= 1
                ans += 1
            while location[0] < points[i][0] and location[1] < points[i][1]:
                location[0] += 1
                location[1] += 1
                ans += 1
            while location[0] > points[i][0]:
                location[0] -= 1
                ans += 1
            while location[0] < points[i][0]:
                location[0] += 1
                ans += 1
            while location[1] > points[i][1]:
                location[1] -= 1
                ans += 1
            while location[1] < points[i][1]:
                location[1] += 1
                ans += 1

        return(ans)