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
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] > amount else dp[amount]

# Solution:
# 把for j in range(len(coins))
# 改为 for coin in coins
# 速度有所提升

# Beats: 52.31%
# Runtime: 1412ms
# medium