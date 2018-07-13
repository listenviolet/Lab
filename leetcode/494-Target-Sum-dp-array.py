class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        dp = [[0] * 2001 for _ in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            for sum in range(-1000, 1001):
                if dp[i - 1][sum + 1000] > 0:
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000]
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000]
                    
        return dp[len(nums) - 1][S + 1000] if S <= 1000 else 0

# Description:
# You are given a list of non-negative integers, a1, a2, ..., an, 
# and a target, S. Now you have 2 symbols + and -. 
# For each integer, you should choose one 
# from + and - as its new symbol.

# Find out how many ways to assign symbols 
# to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

# Note:
# dp[0][nums[0] + 1000] = 1
# dp[0][-nums[0] + 1000] += 1
# 这里第二行一定是 += , 而不是 =
# 虽然初始值dp均为0
# 但是考虑nums[0] = 0
# 那么无论正负，[+-nums[0] +1000] 的值始终为[1000]，
# 那么dp的值应为2 (1 + 1), 而非1。

# Beats：14.34%
# Runtime: 604ms
# medium