class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        LEFT = 0
        RIGHT = 1
        HEIGHT = 2
        output = []
        if not buildings: return output
        left = min(b[LEFT] for b in buildings)
        right = max(b[RIGHT] for b in buildings)
        last_height = None
        
        height = 0
        for i in range(left, right + 1):
            heights = [b[HEIGHT] for b in buildings if b[LEFT] <= i < b[RIGHT]]
            height = max(heights) if heights else 0
            if height != last_height:
                output.append([i, height])
                last_height = height
        return output

# Time Limit Exceeded
# 3/36 test cases passed
