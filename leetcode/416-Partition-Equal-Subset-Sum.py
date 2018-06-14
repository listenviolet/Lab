class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def findSum(num, nums):
            if num in nums: return True
            if len(nums) == 1 or num < nums[0]: return False
            else:
                for i in range(len(nums) - 1):
                    if findSum(num - nums[i], nums[i + 1 :]) == True:
                        return True
                    else:
                        continue
                return False
        
        
        nums.sort()
        Max = nums[-1]
        residual = nums[:-1]
        sum_residual = sum(residual)
        dis = sum_residual - Max
        if dis == 0: return True
        if dis < 0 or dis % 2 != 0: return False
        if dis % 2 == 0:
            return findSum(dis // 2, residual)

# Description:
# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets 
# such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

# Solution:
# 首先想一下，nums分成两组，各组之和相等
# 则这两组中必有一组含有最大的元素
# 最大的元素本身，或与其他小元素的组合 == 剩余元素之和
# 1. max > 剩余元素之和 ：不成立
# 2. max = 剩余元素之和 ：恰好成立
# 3. max < 剩余元素之和 ：需与其他元素组合
#    组合时，需要补充进来的数量为(sum_residual - max) // 2：
#    这样从residual中拿走一部分，补充到max所在组中即可
#    若dis = sum_residual - max不能被2整除，也即不能对半分：不成立
#    若可以，则递归地每次从residual中取小的元素，
#    用findSum函数找，在residual中是否存在某些元素之和为dis // 2
#    若存在，则成立，否则，不成立。

# Beats: 87.19%
# Runtime: 96ms
# medium
