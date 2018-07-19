class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy = []
        for i in range(len(nums)):
            copy.append(nums[i])
        copy.sort()
        start = len(nums)
        end = 0
        for i in range(len(nums)):
            if nums[i] != copy[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end - start >= 0 else 0

# Description:
# Given an integer array, you need to find one continuous subarray 
# that if you only sort this subarray in ascending order, 
# then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order 
# to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, 
# so ascending order here means <=.

# Solution:
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
# Approach #3 Using Sorting [Accepted]
# Algorithm

# We can sort a copy of the given array numsnums, 
# say given by nums_sorted. 
# Then, if we compare the elements of numsnums and nums_sorted, 
# we can determine the leftmost and rightmost elements which mismatch. 
# The subarray lying between them is, 
# then, the required shorted unsorted subarray.

# Complexity Analysis

# Time complexity : O(nlogn). Sorting takes nlognnlogn time.

# Space complexity : O(n). We are making copy of original array.

# Beats: 26.94%
# Runtime: 120ms
# easy