class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if sum[end] - sum[start] == k:
                    count += 1
        return count

# Description:
# Given an array of integers and an integer k, 
# you need to find the total number of continuous subarrays 
# whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] 
# and the range of the integer k is [-1e7, 1e7].

# Solution:
# See in Approach #2 Using Cummulative sum 
# https://leetcode.com/problems/subarray-sum-equals-k/solution/

# Algorithm

# Instead of determining the sum of elements everytime 
# for every new subarray considered, 
# we can make use of a cumulative sum array , sum. 
# Then, in order to calculate the sum of elements 
# lying between two indices, 
# we can subtract the cumulative sum corresponding to the two indices 
# to obtain the sum directly, 
# instead of iterating over the subarray to obtain the sum.

# In this implementation, we make use of a cumulative sum array, sum, such that sum[i] is used to store the cumulative sum of nums array 
# upto the element corresponding to the (i-1)^{th} index. 

# Thus, to determine the sum of elements for the subarray nums[i:j], 
# we can directly use sum[j+1] - sum[i].

# Complexity Analysis

# Time complexity : O(n^2) 
# Considering every possible subarray takes O(n^2) time. 
# Finding out the sum of any subarray takes O(1) time 
# after the initial processing of O(n) 
# for creating the cumulative sum array.

# Space complexity : O(n). 
# Cumulative sum array sumsum of size n+1 is used.

# Time Limit Exceeded.
# 58/80 test cases passed.