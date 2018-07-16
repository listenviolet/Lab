class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        for start in range(0, len(nums)):
            sum = 0
            for end in range(start, len(nums)):
                sum += nums[end]
                if sum == k:
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
# See in Approach #3 Without space
# https://leetcode.com/problems/subarray-sum-equals-k/solution/

# Algorithm

# Instead of considering all the start and end points and then 
# finding the sum for each subarray corresponding to those points, 

# we can directly find the sum on the go 
# while considering different end points. 
# i.e. We can choose a particular start point 
# and while iterating over the endend points, 
# we can add the element corresponding to the end point 
# to the sum formed till now. 

# Whenver the sum equals the required k value, 
# we can update the countcount value. 
# We do so while iterating over all the endend indices possible 
# for every startstart index. 
# Whenver, we update the startstart index, 
# we need to reset the sumsum value to 0.


# Complexity Analysis

# Time complexity : O(n^2).
# We need to consider every subarray possible.
# Space complexity : O(1). Constant space is used.

# Time Limit Exceeded
# 58/80 test cases passed.