class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        # sell = [0] * n
        cursell = 0
        prevsell = 0
        
        # buy = [0] * n
        # buy[0] = -prices[0]
        buy = -prices[0]
        
        for i in range(1, n):
            tmp = cursell
            cursell = max(cursell, buy + prices[i])
            buy = max(buy, prevsell - prices[i] if i > 1 else -prices[i])
            prevsell = tmp
        return cursell

# Solution:
# 由于sell[i]仅仅依赖前一项，buy[i]仅仅依赖前两项，
# 所以优化到O(1)

# Beats: 74.21%
# Runtime：48ms
# medium