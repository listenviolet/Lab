class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        
        start, end = 0, m
        while start < end:
            midrow = (start + end) // 2
            if matrix[midrow][0] == target:
                return True
            elif target < matrix[midrow][0]:
                end = midrow
            else: start = midrow + 1
        row = start - 1

        l, r = 0, n
        
        while l < r:
            midcol = (l + r) // 2
            if matrix[row][midcol] == target: return True
            elif matrix[row][midcol] < target:
                l = midcol + 1
            else: r = midcol
        return False

# Description:
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer 
# of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

# Solution:
# 在行、列依次用二分法查找

# Beats: 41.43%
# Runtime: 48ms
# medium