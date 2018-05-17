class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        maxsqlen = 0
        prev = 0
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]       #上一行的dp[j]值
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        
        return maxsqlen * maxsqlen
                
# Solution:
# 首先，确定下来目标格子的上，左，左上格子的dp-即最大正方形边长后，
# min + 1即为当前格子的最大边长
# 比如下图

# ***
# *AB
# *Co

# A为2即左上四个小格子为1
# B为2即右上四个小格子为1
# C为2即左下四个小格子为1
# 这样，如果o为1,则这九个格子均为1，边长变为3
# 所以如果dp为二维矩阵的话，核心的式子为：
# 若当前格子为1，则以该格子为左下角的大正方形的边长为：
# min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
# #######################

# Better dp
# 看上面的式子，每次对于新的一列的更新，都是在来到新的一行之后更新的

# prev       dp[j]
# dp[j - 1]  new_dp[j]

# 核心式子：
# dp[j] = min(dp[j - 1], prev, dp[j]) + 1

# prev为保留的上一行的d[i - 1][j - 1]
# dp[j - 1]为这一行刚刚更新后的d[i][j - 1]
# 等号右边的dp[j]为上一行的dp[i - 1][j]
# 这样就不需要用二维数组进行记录了，
# 因为都是在下一行时，对上一行进行更新
# 上一行的dp[j]保留为temp,为下一个dp[j]计算时的prev

# Beats: 97.52%
# Runtime: 80ms
# medium     