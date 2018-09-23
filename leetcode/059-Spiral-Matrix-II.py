class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [([0] * n) for _ in range(n)]
        cnt = 1
        r = 0
        while n >= 2:
            for i in range(n - 1):
                matrix[r][r + i] = cnt
                cnt += 1
            for i in range(n - 1):
                matrix[r + i][r + n - 1] = cnt
                cnt += 1
            for i in range(n - 1):
                matrix[r + n - 1][r + n - 1 - i] = cnt
                cnt += 1
            for i in range(n - 1):
                matrix[r + n - 1 - i][r] = cnt
                cnt += 1

            n -= 2
            r += 1
        if n == 1:
            matrix[r][r] = cnt
        return matrix

# Description:
# Given a positive integer n, 
# generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# Solution:
# 用r标记圈数
# 1  2  3  | 4
# -------- |
# 12| 13 14| 5
# 11| 16 15| 6
# 10| 9  8   7
#    ---------

# 注意当n == 1时，for循环中n - 1 = 0，则不能执行，
# 如input = 3 时，9不能输出，
# 所以需要单独写 n == 1 时的情况。

# Beats: 48.93%
# Runtime: 44ms
# medium