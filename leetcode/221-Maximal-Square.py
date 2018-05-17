class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        Max = 0
        
        def square(row, col, length): # length 为原来边长
            flag = 1
            if row + length >= m or col + length >= n: return length
            for i in range(row, row + length + 1):
                if matrix[i][col + length] == '0':
                    flag = 0
                    break
            if flag == 1:
                for j in range(col, col + length):
                    if matrix[row + length][j] == '0':
                        flag = 0
                        break
            if flag == 1:
                length += 1
                return square(row, col, length)
            elif flag == 0:
                return length

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1' and m - i >= Max:   
                    temp = square(i, j, 1)
                    if temp > Max: Max = temp
                
        return Max * Max

# Description:
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

# Solution:
# ooxx*oo
# ooxx*oo
# oo***oo
# 即square函数中row,col为已探测出的正方形的左上角坐标
# 再探测以row,col为顶点的正方形时
# 即需要探测*所示位置
                     
# Beats: 14.88%
# Runtime: 212ms
# medium            