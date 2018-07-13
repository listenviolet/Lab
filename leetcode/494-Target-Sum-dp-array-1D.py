class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        dp = [0] * 2001
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            next = [0] * 2001
            for sum in range(-1000, 1001):
                if dp[sum + 1000] > 0:
                    next[sum + nums[i] + 1000] += dp[sum + 1000]
                    next[sum - nums[i] + 1000] += dp[sum + 1000]
            dp = next
                    
        return dp[S + 1000] if S <= 1000 else 0

# Description:
# You are given a list of non-negative integers, a1, a2, ..., an, 
# and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

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

# Solution:
# Approach #4 1D Dynamic Programming [Accepted]:
# Algorithm

# If we look closely at the last solution, 
# we can observe that for the evaluation of the current row of dpdp, 
# only the values of the last row of dpdp are needed. 
# Thus, we can save some space by using a 1D DP array 
# instead of a 2-D DP array. 
# The only difference that needs to be made is 
# that now the same dpdp array will be updated for every row traversed.

# Beats: 27.86%
# Runtime: 464ms
# medium