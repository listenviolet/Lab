class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums[:] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        def divide(nums, dp, low, high):
            if low + 1 == high: return 0
            if dp[low][high] > 0: return dp[low][high]
            ans = 0

            for i in range(low + 1, high):
                ans = max(ans, nums[low] * nums[i] * nums[high] + divide(nums, dp, low, i) + divide(nums, dp, i, high))
            dp[low][high] = ans
            return ans
  
        return divide(nums, dp, 0, n - 1)

# Solution:
# 考虑分治法来处理的时候，
# 如果选择以某个气球为分割点，
# 那么其左边部分和右边部分都要依赖与那个气球，
# 因此我们不能让这个气球先爆．
# 也就是说我们选择分割点的时候不是选择先爆的气球，
# 而是最后爆的气球，这样分成的左右两个部分将相互独立．
# 即如果最后只剩下气球i，
# 那么其最后只依赖与第０和ｎ－１个气球，
# 而在[0, i] 和 [i, n-1]两个区间是相互独立的，
# 这样我们就可以将问题分割为相互独立的子集．
# 这样时间复杂为O(n^n). 
# 但是在枚举各个分割点的时候会有很多重复的计算，
# 因此我们可以保存已经计算过的区间．
# 这样时间复杂度可以优化到O(n^3).

# Beats: 30.85%
# Runtime: 756ms
# hard