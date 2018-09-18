class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else: col -= 1
            else: return False

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
# 从右上到左下查找matrix，
# 若当前 > target, 则向前一列查找 => 则矩阵后几列均不用再考虑
# 若当前 < target, 则向下一行查找 => 则矩阵前几行均不用再考虑

# Beats: 41.67%
# Runtime: 48ms
# medium