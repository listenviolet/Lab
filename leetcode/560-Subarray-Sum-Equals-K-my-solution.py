class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = []
        if nums is None: return 0
        sum = 0
        for n in nums:
            l = [i + n for i in l]
            l.append(n)
            sum += l.count(k)
        return sum

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

# My solution
# Time Limit Exceeded.
# 58/80 test cases passed.