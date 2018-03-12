class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # If we try to move the pointer at the longer line inwards, 
        #we won't gain any increase in area, 
        #since it is limited by the shorter line. 
        #But moving the shorter line's pointer could turn out to be beneficial, 
        #as per the same argument
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_area = max((r - l) * min(height[l], height[r]), max_area)
            if height[l] > height[r]: r = r - 1
            else: l = l + 1
        return max_area