class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in xrange(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        tmp = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res

# 同样思路
# 初始化时，直接将res置为1，res[0] = 1,
# 相当于之前的tmp
# xrange 用法与 range 完全相同，
# 所不同的是生成的不是一个list对象，而是一个生成器。

# Beats: 70.66%
# Runtime: 170ms
# medium
