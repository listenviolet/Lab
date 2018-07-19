class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Min = max(nums)
        Max = min(nums)
        
        flag = False
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag == True:
                Min = min(Min, nums[i])
        
        flag = False
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag == True:
                Max = max(Max, nums[i])
        
        l = 0
        r = len(nums) - 1
        while l < len(nums):
            if Min < nums[l]:
                break
            l += 1
        
        while r >= 0:
            if Max > nums[r]:
                break
            r -= 1
        
        return r - l + 1 if r - l >= 0 else 0

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

# Approach #5 Without Using Extra Space [Accepted]:

# Algorithm

# The idea behind this method is that 
# the correct position of the minimum element in the unsorted subarray 
# helps to determine the required left boundary. 
# Similarly, the correct position of the maximum element 
# in the unsorted subarray helps to determine the required right boundary.

# Thus, firstly we need to determine when the correctly sorted array goes wrong. 
# We keep a track of this by observing rising slope starting from the beginning of the array. 
# Whenever the slope falls, we know that the unsorted array has surely started. 
# Thus, now we determine the minimum element found 
# till the end of the array numsnums, given by minmin.

# Similarly, we scan the array numsnums in the reverse order 
# and when the slope becomes rising instead of falling, 
# we start looking for the maximum element 
# till we reach the beginning of the array, given by maxmax.

# Then, we traverse over nums and determine the correct position of min 
# and max by comparing these elements with the other array elements. 
# e.g. To determine the correct position of minmin, 
# we know the initial portion of numsnums is already sorted. 
# Thus, we need to find the first element which is just larger than min. 
# Similarly, for maxmax's position, 
# we need to find the first element 
# which is just smaller than maxmax searching in numsnums backwards.

# Beats: 11.80%
# Runtime: 148ms
# easy