class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = sums = 0
        cnt = collections.Counter()
        for num in nums:
            cnt[sums] += 1
            sums += num
            ans += cnt[sums - k]
        return ans

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
# Keep tracking the prefix sums and their counts using hashmap.

# s -> count: how many arrays nums[0:j] (j < i) that has sum of s

# s = sum(nums[0:i])

# check how many arrays nums[0:j] (j < i) that has sum (s – k)

# then there are the same number of arrays nums[j+1: i] that have sum k.

# Time complexity: O(n)

# Space complexity: O(n)

# Beats: 21.23%
# Runtime: 88ms
# medium