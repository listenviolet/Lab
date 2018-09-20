class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 1
        Max = max(nums)
        flag = [0] * Max
        print(flag)
        
        for i in nums:
            if i > 0:
                flag[i - 1] = 1
        print(flag)
        
        for i in range(len(flag)):
            if flag[i] == 0:
                return i + 1
        return Max + 1

# Description:
# Given an unsorted integer array, 
# find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

# Solution:
# 本题要求查找丢失的最小的正整数。
# 由于要求在O(n)时间内解决，故不可以直接对原数组排序；
# 构建一个辅助数组flag，数组的序号对应1到Max(原数组最大值)，数组值初始化为0，
# 通过一次遍历原数组，将原数组中出现过的数字在flag数组中对应位的值置为1；
# 如原数组中有数组3，则在flag[3 - 1] 置为1；
# 最后通过遍历一次辅助数组，找到第一个值为0的flag[i],
# 表示原数组中缺失(i + 1)这个正整数。

# Beats: 85.91%
# Runtime: 40ms
# hard