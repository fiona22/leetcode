# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = []

        for j in range(0, len(height)-1):
            for k in range(j+1, len(height)):
                if height[k] > height[j]:
                    area = height[j]*(k-j)
                else:
                    area = height[k]*(k-j)
                areas.append(area)
        return max(areas)

sol = Solution()

print sol.maxArea([1,8,6,2,5,4,8,3,7])