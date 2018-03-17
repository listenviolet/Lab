class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        n = len(height)
        
        for i in range (1, n - 1):
            max_left, max_right = 0, 0
            for j in range (i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range (i, n):
                max_right = max(max_right, height[j])
            
            ans += min(max_left, max_right) - height[i]
        return ans