class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Max = []
        if not nums: return Max
        if k >= len(nums): 
            Max.append(max(nums))
            return Max
        
        for i in range(len(nums) - k + 1):
            Max.append(max(nums[i: i + k]))
        return Max

# Description:
# Given an array nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position. 
# Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note: 
# You may assume k is always valid, 
# 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?


# Solution:
# 每次移动后求k窗口内最大值

# Beats: 10.94%
# Runtime: 843ms
# hard

