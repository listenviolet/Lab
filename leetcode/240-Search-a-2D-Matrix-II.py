class Solution:
    def find(self, target, row):
        a, b = 0, len(row)
        m = (a + b) // 2
        while(a < b):
            if target == row[m]: return True
            elif row[m] > target: 
                b = m
                m = (a + b) // 2
                continue
            elif row[m] < target:
                a = m + 1
                m = (a + b) // 2
                continue
        return False
    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][n - 1] >= target:
                if(self.find(target, matrix[i]) == True): return True
                else: continue
        return False

# Description
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Example 1:

# Input: matrix, target = 5
# Output: true
# Example 2:

# Input: matrix, target = 20
# Output: false
#########################################

# Solution
# 首先按行搜索：该行第一个元素<= target and 最后一个元素>= target
# 则在该行搜索
# 行内搜索用的是二分查找
# 若该行内没有target, 则按同样方法搜索下一行
# 直到没有使得if条件成立的行，返回False

# Note
# 二分查找时，更新 a = m + 1, 而不是 a = m
##########################################
      
# Beats: 95.84%
# Runtime: 52ms
# medium