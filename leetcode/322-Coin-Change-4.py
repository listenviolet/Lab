class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        M = amount + 1
        dp = [M] * M
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < M else -1

# 这里外层对coin的情况遍历
# 每次用一个新的coin替换，看min的变化
# 减少了判断，i也是从coin到amount
# 提升了速度

# Beats: 62.27%
# Runtime: 1284ms
# medium