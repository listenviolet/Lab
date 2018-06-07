class Solution:
    ans = -1
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        self.ans = amount + 1
        
        def coinchange(coins, start, amount, count, ans):
            if amount == 0:
                self.ans = min(self.ans, count)
                return
            if start == len(coins): return
            
            coin = coins[start]
            k = amount // coin
            while k >= 0 and count + k < ans:
                coinchange(coins, start + 1, amount - k * coin, count + k, self.ans)
                k -= 1
        
        coinchange(coins, 0, amount, 0, self.ans)
        return self.ans if self.ans < amount + 1 else -1

# Solution:
# http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-322-coin-change/
# 本题最快的解法是DFS
#                       [5,2,1] 11, 0
#                    2*5 /    1*5|
#                       /        |
#              [2,1] 1, 2    [2,1] 6,1 
#                 0*2 /          |
#                    /       (之后的amount 6除以任何coin， 
#             [1] 1,2         所用硬币总数都大于第一个分支的3，
#              1*1 /          故剪枝)
#                 /
#           [] 0, 3

# 这里第一项数组是可用的coin的数组，每次取尽量多的最大的coin
# 第二项是剩余的amount
# 第三项是已用的硬币数量

# def coinchange(coins, start, amount, count, ans)中
# coins为题目的coins数组
# start为新的起始硬币ind
# amount为剩余总额
# count为已用硬币总数
# ans为DFS一个分支后所得的表示完全amount共需硬币数量

# Note:
# 这里不可以直接在def coinChange中定义并传递参数ans,
# 它并不会把变化后的值传入调用的函数
# 所以在class中定义了ans
# 在def coinChange中用self.ans对其赋初值

# Beats: 99.54%
# Runtime: 156ms
# medium