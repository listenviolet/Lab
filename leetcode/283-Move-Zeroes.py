class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        notzero = -1
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                notzero += 1
                nums[notzero] = nums[i]
            elif nums[i] == 0:
                zero += 1
        if zero > 0:
            for i in range(notzero + 1, notzero + zero + 1):
                nums[i] = 0

# Descriptiion:
# Given an array nums, 
# write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Solution:
# 遍历一遍nums，
# 用notzero记录非零元素数（从0开始），
# notzero的值即为这些非零元素之后移动到目标位置的index
# 用zero记录0元素的个数（从1开始），
# zero数即为之后在nums的notzero之后补充的0的个数

# Beats: 99.30%
# Runtime: 48ms
# easy