class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0: 
            flag = -1
            x = -1 * x
        
        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x // 10
        print(nums)
        if not nums: return 0
        i = 0
        while nums[i] == 0 and i < len(nums):
            i += 1
        ans = 0
        for ind in range(i, len(nums)):
            ans = ans * 10 + nums[ind]
            if ans > 2147483647: return 0
        return flag * ans

# Description:
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment 
# which could only store integers within the 32-bit signed integer 
# range: [−231,  231 − 1]. 
# For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.

# Solution:
# 首先用flag标记正负数，之后，取其数字位，转换为list形式
# 用i标记第一个不是0的位
# 将list存储的转换为integer
# Notice:
# 需要保证integer在32位范围内： [-2147483648,2147483647]
# 最后，将转换后的integer * 正负符号即可。

# Beats: 16.48%
# Runtime: 64ms
# easy