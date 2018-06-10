class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return heapq.nlargest(k, counter, key = lambda x: counter[x])

# Description:
# Given a non-empty array of integers, 
# return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size.

# Solution:
# 将python的collection.Counter与heapq结合

# Beats：94.43%
# Runtime: 52ms
# medium