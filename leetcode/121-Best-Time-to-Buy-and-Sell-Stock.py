class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        Max = [0] * len(prices)
        if n == 0 or n == 1: return 0
        def M():
            Max[n - 1] = prices[n - 1]
            for i in range(n - 2, -1, -1):
                if prices[i] > Max[i + 1]:
                    Max[i] = prices[i]
                else:
                    Max[i] = Max[i + 1]
        
        profit = 0
        M()
        for i in range(n - 2, -1, -1):
            temp = Max[i + 1] - prices[i]
            if temp > profit:
                profit = temp
        return profit

# Question
# Say you have an array for which the ith element 
# is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction 
# (i.e., buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) 
# and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, 
# i.e. max profit = 0.

# Solution:
# 从左至右找从当前i到(n - 1)元素中最大的元素，存在Max数组中
# 比较Max[i + 1] 与 当前prices[i]之差即为当前卖出最大profit
# 取各个profit的最大值
# beats: 88.69%