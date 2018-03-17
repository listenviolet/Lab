class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        ans = 0
        n = len(height)
        
        left_max = [None] * n
        right_max = [None] * n
        
        left_max[0] = height[0]
        for i in range (1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n -1] = height[n - 1]
        for i in range (n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        for i in range (0, n):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans