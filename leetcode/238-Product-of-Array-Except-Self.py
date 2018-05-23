class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res

# Description
# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to 
# the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? 
# (The output array does not count as extra space 
# for the purpose of space complexity analysis.)

# Solution
# 第一个tmp存的是该元素之前的各元素的乘积
# 第二个tmp存的是该元素之后的各元素的逆序乘积
# res获取的是之前的tmp的值
# 故之前*之后即为最终的res数组的值

# Beats: 16.84%
# Runtime: 210ms
# medium