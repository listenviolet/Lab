class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = 0
        ret = []
        if not matrix or not matrix[0]:
            return ret
        m, n = len(matrix), len(matrix[0])
        while m >= 1 and n >= 1:
            for i in range(n):
                ret.append(matrix[r][r + i])
            for i in range(m - 1):
                ret.append(matrix[r + 1 + i][r + n - 1])
            
            if m > 1:
                for i in range(n - 1):
                    ret.append(matrix[r + m - 1][r + n - 1 - 1 - i])
            if n > 1:
                for i in range(m - 2):
                    ret.append(matrix[r + m - 1 -1 - i][r])
            m -= 2
            n -= 2
            r += 1
        return ret

# Description:
# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Solution:
# r = 0:
# 1->2->3->4

# 8->12

# 11->10->9

# 5

# r = 1:
# 6->7

# 避免再次回转到6，应加入判断条件：m > 1
# 对于
# 7
# 8
# 9
# 避免再次回转到7，应加入判断条件：n > 1

# Beats: 75.70%
# Runtime: 36ms
# medium
