class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        presub = [1]
        cursub = []
        M = nums[0]
        for i in range(len(nums)):
            cursub.append(nums[i])
            for j in presub:
                cursub.append(nums[i] * j)
            M = max(M, max(cursub))
            presub = []
            presub.append(min(cursub))
            presub.append(max(cursub))
            cursub = []
        return M
            
# Question:
# Given an integer array nums, 
# find the contiguous subarray within an array 
# (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, 
# because [-2,-1] is not a subarray.

# Solution:
# 考虑一个例子：
# -2 3 -4 -5
# 当遍历2时：只有 -2
# 当遍历3时，有[3, -2*3]
# 当遍历-4时，有[-4, 3*(-4), -2*3*(-4)] = [-4, -12, 24]
# 当遍历-5时，有[-5, -4*(-5), -12*(-5), 24*(-5)] = [-5, 20, 60, -120]
# 取这些数组中的最大值即为最大乘积
# 这会超时
# 其实presub中不需要保存之前所有的结果，
# 考虑后一个只能是正负两种，
# 则presub中保存最负的和最正的即可
# 避免判断麻烦，可以取min 和 max
# 这样，presub中简化为只有2个数
# 复杂度也降低为O(2*N)

# Beats: 17.55%
# medium
