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
        coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i: dp[i] = min(dp[i], dp[i - coin] + 1)
                else:
                    break
                    
        return -1 if dp[amount] > amount else dp[amount]

# Solution:
# 这里先对coins排序，然后依次试coin
# 如果coin > i, 则结束结束对coin的遍历

# Beats: 57.87%
# Runtime: 1376ms
# medium