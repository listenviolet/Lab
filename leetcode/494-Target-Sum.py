class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def calculate(nums, i, sum, S, memo):
            if i == len(nums):
                if sum == S:
                    return 1
                else:
                    return 0
            else:
                if memo[i][sum + 1000] != -1:
                    return memo[i][sum + 1000]
                add = calculate(nums, i + 1, sum + nums[i], S, memo)
                subtract = calculate(nums, i + 1, sum - nums[i], S, memo)
                memo[i][sum + 1000] = add + subtract
                return memo[i][sum + 1000]
        
        count = 0
        memo = [[-1] * 2001 for _ in range(len(nums))]
        
        return calculate(nums, 0, 0, S, memo)

# Description:
# You are given a list of non-negative integers, 
# a1, a2, ..., an, and a target, S. 
# Now you have 2 symbols + and -. 
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

# Solution:
# See Solution: https://leetcode.com/problems/target-sum/solution/
# Approach #2 Recursion with memoization [Accepted]
# Algorithm

# It can be easily observed that in the last approach, 
# a lot of redundant function calls could be made 
# with the same value of i as the current index 
# and the same value of sum as the current sum, 
# since the same values could be obtained 
# through multiple paths in the recursion tree. 
# In order to remove this redundancy, 
# we make use of memoization as well to store the results 
# which have been calculated earlier.

# Thus, for every call to calculate(nums, i, sum, S), 
# we store the result obtained in memo[i][sum + 1000]. 
# The factor of 1000 has been added 
# as an offset to the sum value to map all the sums possible 
# to positive integer range. 
# By making use of memoization, 
# we can prune the search space to a good extent.

# Note:
# memo[i][sum+1000] 表示在index = i时，可以取到sum的不同的组合的个数。
# eg. memo[5][3 + 1000] = 5 表示index = 5时，和为3的组合有5种。
#     memo[5][2 + 1000] = 6 表示index = 5时，和为2的组合有6种。

# Beats: 44.57%
# Runtime: 360ms
# medium