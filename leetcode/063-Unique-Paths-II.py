from math import factorial
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        if not obstacleGrid or not obstacleGrid[0]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        pathNum = [[0] * (n + 1) for _ in range(m + 1)]
        # print(pathNum)
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 1 and j == 1 and obstacleGrid[i - 1][j - 1] == 0:
                    pathNum[i][j] = 1
                elif obstacleGrid[i - 1][j - 1] == 1:
                    pathNum[i][j] = 0
                else:
                    pathNum[i][j] = pathNum[i - 1][j] + pathNum[i][j - 1]
        return pathNum[m][n]

# Description:
# A robot is located at the top-left corner of a m x n grid 
# (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid 
# (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. 
# How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Solution:
# pathNum[i][j] 对应于 走到obstacleGrid[i - 1][j - 1]位置时的总路径。
# 可初始化pathNum为0矩阵，其第0行，第0列均为0，
# pathNum[i][j] = pathNum[i - 1][j] + pathNum[i][j - 1] 
# 当i = 1, 或j = 1时，对应于走到obstacleGrid的边界情况。
# 走到每个位置 i,j 处的总路径 = (走到i - 1,j 路径) + (i, j - 1路径)
# 
# 当obstacleGrid为1时，对应的将pathNum置为0

# Beats: 99.59%
# Runtime: 36ms
# medium